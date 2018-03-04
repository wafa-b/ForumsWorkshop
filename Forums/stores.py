import  itertools
class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self,member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self,id):
        all_members = self.get_all()
        for member in all_members:
            if member.id == id:
                return member

    def update(self,member):
        result = member
        all_members = self.get_all()

        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                break

        return result

    def delete(self,id):
      member = self.get_by_id(id)
      MemberStore.members.remove(member)

    def entity_exists(self,member):
        if self.get_by_id(member.id):
            return True
        return False

    def get_by_name(self, member_name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = self.get_all()
        for member, post in itertools.product(all_members, all_posts):
            if member.id is post.member_id:
                member.posts.append(post)
        for member in all_members:
            yield member

    def get_top_two(self, post_store):
        all_members = self.get_members_with_posts(post_store)
        all_members = sorted(all_members, key=lambda x: len(x.posts), reverse=True)
        return all_members[:2]


class PostStore:

    posts = []
    last_id = 1

    def get_all(self):
        return PostStore.posts

    def add(self,post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self,id):
        all_posts = self.get_all()
        for post in all_posts:
            if post.id == id:
                return post

    def update(self,post):
        result = post
        all_posts = self.get_all()

        for index, current_member in enumerate(all_posts):
            if current_member.id == post.id:
                all_posts[index] = post
                break

        return result

    def delete(self,id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def entity_exists(self,post):
        if self.get_by_id(post.id):
            return True
        return False


    def get_by_name(self, post_name):
        all_posts = self.get_all()
        for post in all_posts:
            if post.name == post_name:
                yield post
