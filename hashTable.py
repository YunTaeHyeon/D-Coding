class Node: #연결리스트를 위한 클래스 정의
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class hashTable:
    def __init__(self):
        self.table=[]
        for i in range(26): #알파벳이 26개이기 때문에 Node 26개로 이루어진 배열 생성
            self.table.append(Node(None))

    def hashing(self, key): #해싱함수 정의. 문자열의 첫 문자를 기준으로 하여 인덱싱함
        index=ord(key[0].upper())-65 #아스키코드상에서 "A"가 65이기 때문(대문자만 사용)
        return index
    
    def search(self, key):
        index=self.hashing(key)
        head=self.table[index] #연결리스트 초기값을 저장하기
        
        if head.data == key: #바로 찾았을 경우
            print(key+" 조회 성공")
            return head
        
        else:

            while head.data != None: #찾을 때까지 반복
                if head.data == key:
                    print(key+" 조회 성공")
                    return head
                head=head.next
            print("조회 실패")
            return None #못찾을 경우 None 반환

    def delete(self, key): 
        index=self.hashing(key) #인덱스 찾기
        find=self.search(key) #key를 search한 값 받아오기
        before=None
        head=self.table[index] #연결리스트 초기값 저장

        while self.table[index].data:
            if find.data==self.table[index].data: #찾았다면
                if before==None: #연결된 것이 없이 첫 노드일 경우
                    if self.table[index].next==None: #단일 노드의 경우
                        self.table[index]=Node(None)
                        print(key+" 삭제 성공")

                        return find.data
                    else:
                        self.table[index]=self.table[index].next #삭제될 노드의 다음을 가리키기
                        print(key+" 삭제 성공")
                        
                        return find.data
                else: #첫 노드가 아닐 경우
                    self.table[index]=before
                    self.table[index].next=self.table[index].next.next #before의 다음이 삭제할 노드의 다음을 가리키기
                    print(key+" 삭제 성공")
                    self.table[index]=head #초기값으로 다시 변환

                    return find.data #삭제할 노드 반환

            before=self.table[index]
            self.table[index]=self.table[index].next
        print("삭제 실패")
        return None #삭제할 노드가 없는 경우
        

    def insert(self, key): #키 값을 추가하는 함수
        index=self.hashing(key)
        head=self.table[index] #head를 설정해서 연결리스트 안에서 순차적으로 확인할 수 있도록

        if self.table[index].data==None: #data가 없는 경우
            self.table[index].data=key
            self.table[index].next=Node(None)
            print(key+" 삽입 성공")
        
        else:
            while self.table[index].next: #None이 아니면 None일때까지 반복
                if(self.table[index].data==key): #중복되는 값이 이미 존재하는 경우 None 반환
                    print("이미 존재하는 key")
                    return None
                self.table[index]=self.table[index].next
            self.table[index].data=key
            self.table[index].next=Node(None)
            print(key+" 삽입 성공")
        
        self.table[index]=head #원상복구

table=hashTable()

while(1):
    print("\n해시 테이블\n")
    print("1: 키 값 조회")
    print("2: 키 값 삭제")
    print("3. 키 값 삽입")
    print("4: exit\n")


    num=int(input("번호 입력: "))

    if num==1 or num==2 or num==3:
        key=input("key를 입력: ")
    
    if num==1:
        table.search(key)
    elif num==2:
        table.delete(key)
    elif num==3:
        table.insert(key)
    elif num==4:
        break
    else:
        print("입력 오류")
