"""UserTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.User import User
from models.Post import Post


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            dict(
                firstname="Stanley",
                lastname="Yelnats",
                username="stanyelly",
                email="stantheman@yelnats.com",
                password="stanboy2022",
                company_id=1,
            )
        )

        User.find(1).attach("posts", Post.find(1))
