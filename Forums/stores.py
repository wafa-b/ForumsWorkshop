class MemberStore:

    members = []
    last_id = 0

    def get_all(self):
        return MemberStore.members

    def add(self,member):
        member_id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self,id):
        all_members = self.get_all()
        for member in all_members:
            if member == id:
                return  member

    def update(self,member):
        member = self.get_by_id(id)
        return  member

    def delete(self,id):
      post = self.get_by_id(id)
      return MemberStore.members.remove(member)

    def entity_exists(self,member):
        if self.get_by_id(member_id):
            return True



class PostStore:

    posts = []
    last_id = 0

    def get_all(self):
        all_posts = self.posts
        for post in all_posts:
            return  post

    def add(self,post):
        post_id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self,id):
        all_posts = self.get_all()
        for post in all_posts:
            if post == id:
                return  post

    def update(self,post):
        post = self.get_by_id(id)
        return  post

    def delete(self,id):
        post = self.get_by_id(id)
        return MemberStore.posts.remove(post)

    def entity_exists(self,post):
        if self.get_by_id(post_id):
            return True
