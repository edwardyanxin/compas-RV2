import base64
import os

b64 = b"""iVBORw0KGgoAAAANSUhEUgAAACAAAAEACAYAAADSoXR2AAAABGdBTUEAALGPC/xhBQAAAAlwSFlz
AAAdhQAAHYUB8Bsy7AAAGDlJREFUeF7tWwl4jlfa/kw7RfFPpv1bo9GinW6uVk3p2Fu0HdoqqbWt
KqoosWSItZYIassmQiREUEJGia12CYmICBP71iVaaxVRS5VK73nu873n836rrDX/f333dT3e857z
7Oc55z3v+4XFi+LEK/HZPnVnZy6vNzsLVsq8VG9WVpAxXLKoN3uXnzJoM26mnXMNtvyhfmxmTQrV
ic08LhFsqTsrK6JOfEZVY9gJdWZndrltLPPSs1EZq56anlGjbtzOAFt/fjNhNe4qksxLVGiw2WA2
Xjc2a8+Tkdsa+Yam2YyZxz0FYQMj1srozNNRGZn1YrO+10rUuETDlJvnm/ysAd+QtOVVwlN8DHUK
mo+ZNLpco86srMZkZOqpjH2PhG+r+Vh4ejSFtTFH0sYrh26LIL9SZgIjt/JmXjK6XIPzTkamzehS
kJQGPBqyrQszwmjoII2qtsHLcZIScAGtm5kzupxBD6ncuLWDu+iIOxkndHbdToN1GQmDi0LToBNm
Q5xrxz5PYHDuArSlSM+9b3haYyp2jFqmY9gjoWnrfMPS5lQO2TbXXVaqhGdUpQ6SLkpr8bpZDfSM
TnAJPRKWdqly2DZoeiRk2y+sbo6p8ZDUFnSEDjADqp/G5Cr8E6Vvh1le6QjbtqV6VEZD5YBDjdmq
tFp4erKjoJncpZoRKgciUms4Om8mjr0YnXGUgRqiVnD+a0zPuGZmVJGK12YFJKbWEHOCjO9x5DfI
3H+xTkzW94aIFZybx0LTrygGSal5IxFHAkzCYNqNITswO3Z8YtTsrHU89TjHqk/PsNWawvMztqvU
05jRZQfHTLjKgvTbomQGXfGoVSNOVAlNu8ZlaXRbLLJ/n6UR47ZEwVVDJ6tH7VhsdFksVcPSv2YR
GbclDk7zE5HbDhm3kpqw9FNG0y2MJeZyGvTckrhc2Wct4tsrgm29ijgVDJpthccjtkcZTbfQqdOk
lbnqZzb1vaofbliGM7rAq01Nn/ucnBnYtjwblV5FNe4AV5EynbpPG9B95mnVq0kXOvk82lUKRZFe
AarPlTEXTlGGEbOtYcuKm2XsBK1Upc4QMqeW5Bu27Z/mez0trkDnlEx+i10r1XOmYS4soaOmthMv
wWI17SN7jO47gwKu9gb1ADIMykMqV7d1+s0wrxy2je78QRlw5UB4qp9WaibH9GtHVT24eWR7hBY2
bm2wFp4y+qOVJ/Ukr+b02yKXojW6Cg6rctfbM9MtYxcNnouO6Zd+9VygI47kqVDt4MmBymFpgbL8
LpPHek0LNIYUrP2uyZ1OL7woFvCY5f0+QCe83wccn4re7wOE1u39PuAuQFuK9Nzz7EbFjlHLdHi/
DziBESoHvN8HzHxi1Oysddz7feD2y6z3+4D3+wD5vN8HPEIr1XOmYS4sIe/3ARs5pl87qurBzSPb
I7SwcWuDtfCUUe/3Ae/3gf8KcD7zN6clhGyDSgxcWtxA3K3jFINcgY/reONaaNBwrhCjdNxmqThJ
KFzI1f5OmRyhIk8RjTBKXs2gUWaH5Pi+R6cowww4PR8KCkZA4zRExRrasHZEg/w0TDLzFxqMgIro
hLnqdepJNEboNolOFWj+acidgDbG0wwd4NXsAI3pDHGcmdFOOYI2XNqhME8+jJRKzdCpplI6ao6S
zrDNOddjNOD4jkF5bYM8TqDnuth0AVGAK4GKdUo5xjZBIySOa3nys80rSTtIvbxydTg6ZwMFyEQD
vFIRiY5QOa9URD5CTwFB5zhm5qWsng7qNMu6BaOhMAUpxLbOAKHTzCh0tnSUHCPIS4coy7Z5+vIN
nQEqYtp4TzAC3mvFJPKxT0fHMd5TlmNatsCgIJXxqqNgxITuIzETBK8k7RR5SAWCFmb6SFo5wVTr
dPNKZ9gmP/n0uAbHtB4GoleTHShMRUyZLh4q0dHxnjxs6+ioiLx8TnBZUVYrN/PQAbY10Qnqo6y2
ZYvE0UtNrhwgUTmNm/cO3c8r9VBW95P0dNKeriMbzEwUJNE5CmjwXqdbZ45EGfZpoxrs0/p45fgd
l6EZFNTGWNHae0IbpNPaSY6xX1c/2+YACgQqIHHtUjEVsU2D2imdNbbJo/m1o2yzz1yY+QIjpyCJ
yvTUaNAB8nCMpNt6oyEvU60dJZHnjqACClEBFeoU854R8UpF7CN0Bgga5JiZV49TJ7PAK6fHJcio
U60jJNEJClEhr6xeRkTo6AheOUZHNK8uSpLWzSv7nUCjXNdkoDKdTkJngoqomLw69STek/T8k9fR
CHVSN22Q1wlU7G6J0IiOjIq0YZ1ivVw5xrZ21hWox50dl9BRkfQ+QJgd0MY4RmKE7DNnsdCgUUau
U67BPvPUaGhH2aedLRL0/DrOG43TCXNWNMjL+XaUKTBohC8XJMd0ch4ZLZ1gFswgL1cEC85xrEDQ
Fe+uaBglydVc0zAdpI4SA6Mk3TXoqvfCCy+8KFbcV778vevkqs/8TmSM3ydU7FDGO7av8fPNi9Px
2+WZTnTzYjSaNXnkWok4cdt4JPLO90Leufdc0vWTHZQTIuIyQ5ruuafUDbm+IpRv4OaFKDHSE3ln
O9yRfvsp2iOlrvlIO5FvIO/SDNw63b5YKHlpE52NfAN5Mve3TrYtGp2wUvKSVwrhwPko/Ppdaxu9
+aqvVlKsVKpUqalydQJu/RiJm9+2UrR3fVP85eEKuH5xK/KuZhSYbl3JwKmcFNz8ec8Z0g2hY/vW
nK/0lwf4o2Zzq0l74NaZCNw82kLRxx2qYeyn7WVavkDeD9MKRLcM2p/+GX79Ye5B0ukDkUfGDW9/
ply5Mt8Y9pyAX0+G4saBZjiZ1gQP+JTG2aPxuHVqksxtcMHohJWyNw+SggzdS0pf2e/o36r7nhM7
nazmnIGbxyfj+u6mCPJ/At3ffwl5Z2RVfBtQaMpa8zFufT9i9/mDg7JnTHjj29Kl7+VJ2e0GhhvH
xiM3uR4qPlga+5NH4Naxfrh1uEshqLOiHctkRXzVOzNzRet9zV/2PV3mvntHG7ZcAtf3jkJU/8po
1sBXIgjGr3taCr3tnrI9U1rCq7iS3Xr7gil1D5W+7w9XxcZDVlOugatpA/BM5fuwOrYtft3dBje3
N8DN9PqFppT42ti3tN6Oji0q5ZQtcw/fEzwCy8a9hWcfK4tf9/XDjc3PCj1TJNow40kkhVTbXbbM
Hy6L/upWM+6B11/yRdzouri5rSlurK9SZFo49i/o28Hnq7JlS/EN6o5AxQfK4NquXiL8OG6sEyVF
oF/WVkFIwEN48M/3/Ci6XW48drjv3lII7vt37Jj7GjZOrlgs1OOdP6HsvaXcbjx2+KM4IJeSoPeF
vPDCCy88wnHjKCm4tQMNtq1dJQLDirMdo/suOmAm+YdfP4sVv1k/6drZEXKG9DbOs1hShHKkXeRv
gNRBXdRJ3Ub3nWE4kvOV7xM5oyeP7oLR+RcmL2UoW+RARncaHVRr6c7cvDGiaIy8uo2xsJ2SF2SJ
T+n5ShBJ2uGq7zZPDmUoa6jxCHHQjuyx4bcAy8Y822FSoqvJCMVQULuGiSkktlWfjBlsFpEJt2yE
Kwec7Bl16WYFUIlrRRZLJeknuYJ7OcPabXvGrdHRJi/J8o5E3QrWz+wb5J5ZcAVPDmyCn2V9nvUg
Sl2t0UXpduWAHdE4Gdvk5QrlWFbLdaBMQR0x5EjVxADJ1RhlKEsdVl3WwBzteUQ71LTsFAVDC+EA
ZShLHUXCN2IgB66XoKcpoAxli4y76gCLZ29edqGnYEf+psC+KKzVGm8rnqIXoS7EeKXb0R7/0VAd
74hCVqv2nMtwvRJ0hqcpMC9D6qJO6na056rDDr/HRuRA9nDein3Uthts6ZLYqV0KiW1jK779+2EB
tmKPWNOxecD6iNfUA4gPGuNhwwdPknoGCLHtOM6HUUDPMPNvygWDuGY9FzwgC8pVhG5AHvJWX3FA
P47zdQ4wpwTKsMWSKzeu57cA4EmIuqhTbu3sCNlglIW1MOSfIKE7RptfUBd1sqlh7b4No9vNSig+
GFZcOOBAJYXfy44XXvw/RH6WT354Cg1j+zA2kGbylHMkR55ihqHawYG+csAg/R4OOJAV9ocOOx75
p4jHcQNUZDwZuzidctzck9eQKZoToqCqzTjhxqBxZ3dvcqJwf0klgj6iIFvo9s8sHgwqONxTljqo
y+jKH1waV9125GjQeVxQKCdEgCcix7cao8aNKn9Jqr+5nPdJbDuOm+BGn2sIo53Hcr6rya8hbGqw
baklr1615LSsSL26GaPWccpQVtr0xlVGnWE2zoOlcfrN5clXhq2Gb5PF8pKkn2SF3bhxWraepnmg
vZMT+vCIdlK9JsMifHvufCXSSirdVtg7IC8qMkYeA5S1c4S6xYbxyc4GO8+FkR+a7A1rUPlDHhzg
mMkBDZMj/MtMO3tC9nOnjLuhrB614v0bROZYqolR0jNikKTvH8zLmdmmR7wrWU2O9v47HDCTxymw
ML1iUMNxCtRYwadAIV9F+KAo/18PDnCMPAZMhj0WoQ1cIkJ3ZxlqmJ3gvQj/fhuRhjDeva2YcOOx
VnzbQEk9jAgKODlhb7DkHscaInj3DiQaouDuHclMEF12ZIWjA+74igFGfRsV7upYXsJHc0OtgwOO
VJIOOJA75JfPCy/+76Lxo1WqoH6jV1D9+RdQp+HLeEauTz9XA7Xqv4xKj1Zh5TudiIoTjQM/HYWT
V28i4cuNOJp7A3NWbMCs5eux6dhpfDTw0xJ3ICA8Jg6JazZi93c/4ODFX5TxnT/8jGlL12Fc3GI6
YN6aix1BiWs2qegP5/6CfeevIyZpPTLO/oypX6xF6JK1Je5A/CIxvmD1Rhy48Auyf7yOGcvWIe30
NYSJ8RnrttOB/B27ComUry/dwLxVG7BXos869zOiJPVbTl3FlH+txZffXaED+T96FRS+VavlRi1Y
gk6f9EGszH1S1mEMi4hR0ft1643+U6JRsXJV/tluicCvc6++qvDC5/9LFV78pgwMCY/B+u+v4NPY
RVj27U94s0svZsHxv3sWC+KXpe5UqQ+Zl4jtUnhbT11DiKR+jaR+eEwClnz9EyasSCuZOijv8+fc
/VJ4i1MyVepZeJtPXsWkxDVYmXMZ0an7MXFlGuYfzcVDvsU/DX6t3uuEPUb06WeuIUUKb8OJK5iw
eA2Svr2MRIk+YPpCzDmci1c7fVKs08AjdfYHPftg1e4jmBSfiK0S/aYTV1Xqxy36Eku++QkJxy6h
3/QFmLhxD5paHeD/QyzccdwEZXxc1Cy15geMnay225WHTqnCW3X8MoITvsTiry4hZtdxtPIfgnZD
xiNy3wW8GzytWJyIHz99liq8hOQdmCDRc80PCpuJkbMWYbmkfvTC1RgwYyG6TZiO2IMX0WPq5whM
3IJJ//4RrYMi6USh/+NrvJ/MOwtvkRTepLmJSDUKb61Ev2jvCbzVtRdqv/YWorOOY/ahi5hx4AKm
7juPLuHz0WdRCoKyzuHv7/Yo8KpgypKelcdsRs5ZJG7JxGQxvs0oPKZ+zrYD6CubziSp+o7DJ6Db
Z9MxfsMeTJPUh+45j4kS/fsh89B9wWYEbDyGyn+rTye4Q95xOhpXkOUWvXCJetj0GjwCoyNjbWt+
oxTegNCZ1sKTql8ohTdk/irESvQB8Svx/tgojEn9BuN2n8PonT+gxcipqN8tEP3SzqD5+DkoXa6C
x/8GHF5PDhqp+4+p5zwLj9vtP6Xw1h45jXDZbgeKcaZ+qVT9Iik8rvlB81YhWqX+AkIk+rZB09B1
ZhICNx1D04BgtJ22FK8Oi0Dn1YfRNmEHKr5Qj9lw+lU96WP/fvju8k0slCcdCy/tm7PIku12nmy3
zdt/gPnbD2L18Su2Nb9AoueaHzB3Jabtv4AwI/Vjd51Dv+W78PxbHdBp7ib0TTuNnltPo9GQcLwe
ugQdNpzAX/26ORVn42YtWmJy9GwkyXa778J1bPn6DEZMjVHP+WA5aCzZfxIrZMebsXW/qnqu+d7T
FuDN3kPQLWI+OofNR+Cq3ZL6cxi+4wf4TYxHG4m+qUTfadVhfLj5JJrPXIfaA0NRqd4/6IDTVCR9
bjzng6fF2govWaqe0bf8qDeGzExQ2+3nkvq4wxcx88BF9I1boQpvgkTfa2Ey2k2ei9odeuADid4/
9TR6bDmFpsFxqDcoDO3Wn0DDSYm6IJ1Q1fexKmJ8FpK/OoPtYjwx85Ba89xuh8nD5l9G4QUnpaKr
VH4T2fGeb/Im2o+ZBv+EZIySwhu24yxaSfStI5eiiUTfftEOdNp0Eq2XHUQtif5Pj1enA26/GQQN
HDdFPWyGy3OeRyyu+dlpB9CkTUdUr9OQwtzduK75qY1pJLHNvuzHXqyPJxo1R6fETHRPOYVmYUtQ
V6J/Y952PN9zNOU9/lmHTzkfn9zP4herNR8tR6zX2nbURvmVJD/bKnnIm/1ks/Z4K2Y92kvh1R01
C3+8Xy3DO+ro0rB5C7xQr5Geq6Icsymb8lCNerrwXP89kgswTUX7tmMP6ir8X9R44YUXXtwt8ENz
dtly5flDU1G2Yw111hTK1/cDn9Jly+V+MnEO+oQtwsOPPcF93Pzlm8qCKlbyzb2/fAX9hPP0kOFY
9v88WBEk494jghr5dcbIBVsU+YcmgA5JP53wKVfBJ6fbwFH4Yuc36P9ZFN7rMxRlypXnuKvnB/uy
B40PR723P1Ak954zyrQHzlyFYXM349P5KYrqNG9LQRrJHhYag5X/Po7lu49j8JSZ+DztCAaExHHc
8U3Ir1z5CrmT5yxB3Jp01G3REa16qzOBx2nwe0EOFCM/34Lh85MxJH4Ths9LRsseQ/FKy/fQxK8j
ug8ajZERsxEUGYfm73TA8NBY9Bs3DW16BlK5PqzkNHi1Ob5IP4gV4uzYmEV4d3AIPhw1Q/O4RXz3
8bNU1DQ8bN5mtOkXjG5jY9Ho7XcRtioLnQPHYmhIDCLmL8OIydPQoWtPhMQuQEziKgwY9Rn6jRiH
1VlHxclZynjSrhyMkfNkh0FTEDh7Ax1w/xnH56GKua+9748B0SuVA237j8VHwbHKkadrN0SvcdGY
+uVufDR4HBamH8Wq7O+QlHEI46bHI+XIWWw+fBobDpzEGnl/GBe7GEuzvkVU0hY52nfGGx8FokmH
T/Dwo6qoXcKv9uutVdrf7DYILboPQcdhYZKNZLzdYwiF5H2wPzr0G4WPR4YiLvkAEsSJZWLk07BY
rNl3Qgx/j9V7vlORj4lOQOCkaATIAbZj32Hy9hyEgbPX46811auaywNPfNcxMRgUtxH9o5ajQasP
8dbHg/F6R38KsMCCGsgLx6h5G9Dq4wH4MDAYcSkHkbD9mCrG5btzFNGhIDH+hkQduy4Lc7cehl8X
f5V+ktuVwPTT+OA5G/Hq+70xVFYBHSpdvoKtuitVfRKfLdmOyUmZeKf7QOXEkIi5aNutL/xHTZao
F6L3yEmIXCo1FDkf82WFxG85hFbigF+fIOVAK3/XK8HvuQb/QGDcBrw3JBS9QhbK3Itx6/o3pytl
cPQyTFiaga7Dp2D6umzEbtqPeamHMSLqcyySbCSkH1P1oRyQfuVAZ3+VTQbH1SB6nFZCeMveo9An
chnekPlXkd9fnoyOv/0FtO0zAhO+yMCAiAUIil+NmRv2KiOca218wbYjGCYOzN16yMhAb/iHJajg
mGXR47QScgJi1qJ5V3mdnpaEyk/VcOmloOaLjd/ERMlA6Iqd6D4yDNHr92KO1EL/8VFi+CgWCs1P
PYKhU+epflKDZn5qV+WSHiRZriDTbehTqPq4vDZ3GR+v0vNK+56o8MDDdMBlpT5QsVLupGU7lANc
DdHr92C2rAhuRtwVSUz90AirA8zQyy3fhd8nw9AuYCz6SpYffVoFaENAw7bd0VjWaK3X3kG1GnXd
Ra+RNDQmCSHiQLcRoZghDszavF8ZZOR0gKn3D46U/gOIkjopc796VuRUebYmnnyxgX7A2VZCku9T
z7ODTDTMb3yenlhBHfqNxJTlmegzQd4hl6apQpyyeCPGxiWpgpwr8z4oLF45Nm0tf0C3m3Ma5luS
LcNcEgX5obkxt2U6wF2x5+hw5QCLrZ/UAdPPta8diHJ2oOjgfkAHwlfvQv/Js2wOsPA4DdoB9peI
A4KUMQs2IXRlFnqMCkPMpn2Ys8W6Erj5zBMHBodbHeBeQX6rWPEh6MOhk5QDXIoxG8UBqXhuPnoV
9B0bicgV29VuKfyeirpQ8Pvzw5XwxHO14Pv403jqhdp4puZLNMRtm9GaiTVWHOdKO3CVuNwnvPAi
/7BY/gM5Ka1JKbIM1gAAAABJRU5ErkJggg=="""

b64_decoded = base64.decodebytes(b64)

HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'grid.png')

with open(FILE, 'wb') as f:
    f.write(b64_decoded)
