import models
import stores


member1 = models.Member("Ahmed",30)
member2 = models.Member("Abdullah",20)


post1 = models.Post("First Post","This is first post")
post2 = models.Post("Second Post","This is second post")
post3 = models.Post("Third Post","This is third post")


member_store = stores.MemberStore()
member_store.add(member1)
member_store.add(member2)

print(member_store.get_all())

print member1
print member2

print post1
print post2
print post3
