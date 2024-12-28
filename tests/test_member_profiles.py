import pytest
from src.member_profiles.member_profile_manager import MemberProfileManager
from src.member_profiles.member_profile import MemberProfile


@pytest.fixture
def member_profile_manager():
    # Initialize the MemberProfileManager with a test CSV file
    return MemberProfileManager(csv_file="../data/member_profiles.csv")


def test_add_member_profile(member_profile_manager):
    profile = MemberProfile(
        id=4,
        name="Emily Davis",
        age=32,
        gender="Female",
        membership_type="Regular",
        health_info="No health issues",
        membership_status="Active"
    )
    member_profile_manager.add_member_profile(profile)


def test_remove_member_profile(member_profile_manager):
    profile = MemberProfile(
        id=4,
        name="Emily Davis",
        age=32,
        gender="Female",
        membership_type="Regular",
        health_info="No health issues",
        membership_status="Active"
    )
    member_profile_manager.add_member_profile(profile)
    member_profile_manager.remove_member_profile(4)


def test_update_member_profile(member_profile_manager):
    profile = MemberProfile(
        id=4,
        name="Emily Davis",
        age=32,
        gender="Female",
        membership_type="Regular",
        health_info="No health issues",
        membership_status="Active"
    )
    member_profile_manager.add_member_profile(profile)

    updated_profile = MemberProfile(
        id=4,
        name="Emily Davis",
        age=33,
        gender="Female",
        membership_type="Premium",
        health_info="No health issues",
        membership_status="Active"
    )
    member_profile_manager.update_member_profile(updated_profile)


def test_load_member_profiles(member_profile_manager):
    profiles = member_profile_manager.load_member_profiles()


def test_save_member_profiles(member_profile_manager):
    profile = MemberProfile(
        id=4,
        name="Emily Davis",
        age=32,
        gender="Female",
        membership_type="Regular",
        health_info="No health issues",
        membership_status="Active"
    )
    member_profile_manager.add_member_profile(profile)
    member_profile_manager.save_member_profiles()
    profiles = member_profile_manager.load_member_profiles()
