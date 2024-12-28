from src.database.csv_handler import read_csv, write_csv
from src.member_profiles.member_profile import MemberProfile

class MemberProfileManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['id', 'name', 'age', 'gender', 'membership_type', 'health_info', 'membership_status']
        self.member_profiles = self.load_member_profiles()

    def load_member_profiles(self):
        data = read_csv(self.csv_file)
        return [MemberProfile.from_dict(item) for item in data]

    def save_member_profiles(self):
        data = [profile.to_dict() for profile in self.member_profiles]
        write_csv(self.csv_file, self.fieldnames, data)

    def add_member_profile(self, profile):
        self.member_profiles.append(profile)
        self.save_member_profiles()

    def remove_member_profile(self, profile_id):
        self.member_profiles = [profile for profile in self.member_profiles if profile.id != profile_id]
        self.save_member_profiles()

    def update_member_profile(self, updated_profile):
        for i, profile in enumerate(self.member_profiles):
            if profile.id == updated_profile.id:
                self.member_profiles[i] = updated_profile
                self.save_member_profiles()
                break