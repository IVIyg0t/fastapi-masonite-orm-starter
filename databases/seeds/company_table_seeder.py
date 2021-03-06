"""CompanyTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Company import Company
from models.User import User


class CompanyTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        Company.create(
            dict(
                name="Holes",
                address="777 Desert Road",
                city="Sierra Nevada",
                state="California",
                phone="123-456-7890",
            )
        )
