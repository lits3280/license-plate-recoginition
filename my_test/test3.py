# coding=utf-8
"""
@Author:lts
@Time:2024/3/15 14:34
@description:
"""
s="""
皖	A,B,C,D,E,F,G,H,J,K,L,M,N,P,R,S
京	A,B,C,D,E,F,G,H,I,J,K,L,N,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
渝	A,B,C,D,E,F,G,H,I,J,K,L,N,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
闽	A,B,C,D,E,F,G,H,J,K
甘	A,B,C,D,E,F,G,H,J,K,L,M,N,P
粤	A,B,C,D,E,F,G,H,J,K,L,N,N,P,Q,R,S,T,U,V,W,X,Y
桂	A,B,C,D,E,F,G,H,J,K,L,M,N,P,R
贵	A,B,C,D,E,F,G,H,J
琼	A,B,C,D,E,F
冀	A,B,C,D,E,F,G,H,J,R,T
豫	A,B,C,D,E,F,G,H,J,K,L,M,N,P,Q,R,S,U
黑	A,B,C,D,E,F,G,H,J,K,M,N,P,R,L
鄂	A,B,C,D,E,F,G,H,J,K,L,M,N,P,Q,R,S
湘	A,B,C,D,E,F,G,H,J,K,L,M,N,U,S
吉	A,B,C,D,E,F,G,H,J,K
苏	A,B,C,D,E,F,G,H,J,K,L,M,N
赣	A,B,C,D,E,F,G,H,J,K,L,M
辽	A,B,C,D,E,F,G,H,J,K,L,M,N,P
蒙	A,B,C,D,E,F,G,H,J,K,L,M
宁	A,B,C,E
青	A,B,C,D,E,F,G,H
鲁	A,B,C,D,E,F,G,H,J,K,L,M,N,P,Q,R,S,U,Y,V
晋	A,B,C,D,E,F,H,J,K,L,M
陕	A,B,C,D,E,F,G,H,J,K,V
沪	A,B,C,D,E,F,G,H,I,J,K,L,N,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
川	A,B,C,D,E,F,G,H,J,K,L,N,Q,R,S,T,U,V,W,X,Y,Z
津	A,B,C,D,E,F,G,H,I,J,K,L,N,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
藏	A,B,C,D,E,F,G
新	A,B,C,D,E,F,G,H,J,K,L,M,N,P,Q,R
云	A,C,D,E,F,G,H,J,K,L,M,N,P,Q,R,S
浙	A,B,C,D,E,F,G,H,J,K,L
"""


counter=0
for line in s.split("\n"):
    if not line:
        continue
    vaild_chars=[x for x in line.split("\t")[1].split(",") if x!='O']
    print(vaild_chars)
    counter+=len(vaild_chars)
print(counter)


print(32*26)
