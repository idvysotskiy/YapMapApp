# file: locators.py

class Tutorial:
    SKIP = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_button"]'
    PAGE_CONTROLS = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_piv"]'
    IMAGE_1 = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_fragment_page_1_image"]'
    TEXT_1 = '//*[contains(text(), "Are you lonely?"]'
    IMAGE_2 = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_fragment_page_2_image"]'
    TEXT_2 = '//*[@text="You can create a group of interest. Invite friends. And to be always in the stream of life."]'
    IMAGE_3 = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_fragment_page_3_image"]'
    TEXT_3 = '//*[@text="Create an event and invite people to spend time together."]'
    IMAGE_4 = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_fragment_page_4_image"]'
    TEXT_4 = '//*[@text="Communicate. Enjoy life. Share your impressions."]'
    IMAGE_5 = '//*[@resource-id="com.yapmap.yapmap:id/activity_welcome_fragment_page_5_image"]'
    TEXT_5 = '//*[@text="And besides, your application will help you find clients in case you are running a business."]'


class Main:
    # BASE
    BACK_BUTTON = '//*[@content-desc="Back"]'
    # LOGIN
    SIGNUP = '//*[@resource-id="com.yapmap.yapmap:id/sign_up_button"]'
    SIGNIN = '//*[@resource-id="com.yapmap.yapmap:id/sign_in_button"]'
    LOGO = '//*[@resource-id="com.yapmap.yapmap:id/activity_login_fragment_main_icon"]'
    TITLE = '//*[@resource-id="com.yapmap.yapmap:id/activity_login_fragment_main_title"]'
    DESCRIPTION = '//*[@resource-id="com.yapmap.yapmap:id/activity_login_fragment_main_description"]'


class Registration:
    # NEW ACCOUNT SCREEN
    # STEP 1/4
    EMAIL = '//*[@resource-id="com.yapmap.yapmap:id/email_edit_text"]'
    ERROR = '//*[@resource-id="com.yapmap.yapmap:id/textinput_error"]'
    INVITE_CODE = '//*[@resource-id="com.yapmap.yapmap:id/invite_code_edit_text"]'
    SIGN_UP = '//*[@resource-id="com.yapmap.yapmap:id/sign_up_button"]'
    TETMS_SWITCH = '//*[@resource-id="com.yapmap.yapmap:id/terms_switch"]'
    TERMS_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/terms_text_view"]'
    SHOW_PASSWORD = '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text_layout"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageButton[1]'
    SHOW_CONFIRM_PASSWORD = '//*[@resource-id="com.yapmap.yapmap:id/confirm_password_edit_text_layout"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageButton[1]'
    PASSWORD = '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text"]'
    CONFIRM_PASSWORD = '//*[@resource-id="com.yapmap.yapmap:id/confirm_password_edit_text"]'
    TITLE = '//*[@resource-id="com.yapmap.yapmap:id/new_account_text_view"]'
    DESCRIPTION = '//*[@text="Please enter all the information"]'
    CURRENT_STEP = '//*[@resource-id="com.yapmap.yapmap:id/current_text_view"]'
    ALL_STEP = '//*[@resource-id="com.yapmap.yapmap:id/all_text_view"]'
    STEPS_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/text_view"]'
    POPUP = "//*[text() = 'You must agree with terms']"

    # STEP 2/4
    UPLOAD_PICTURE_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/profile_title_text_view"]'
    UPLOAD_PICTURE = '//*[@resource-id="com.yapmap.yapmap:id/profile_photo_layout"]/android.widget.FrameLayout[1]'
    FIRST_NAME = '//*[@resource-id="com.yapmap.yapmap:id/first_name_edit_text"]'
    LAST_NAME = '//*[@resource-id="com.yapmap.yapmap:id/last_name_edit_text"]'
    DOB_TITLE = '//*[@resource-id="com.yapmap.yapmap:id/dob_title"]'
    DOB_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/dob_text_view"]'
    DOB_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/dob_layout"]'
    GENDER_TITLE = '//*[@resource-id="com.yapmap.yapmap:id/gender_title_text_view"]'
    MALE = '//*[@resource-id="com.yapmap.yapmap:id/male_text_view"]'
    FEMALE = '//*[@resource-id="com.yapmap.yapmap:id/female_text_view"]'
    CONTINUE = '//*[@resource-id="com.yapmap.yapmap:id/continue_button"]'
    PERMISSION_TITLE = '//*[@resource-id="com.android.permissioncontroller:id/permission_message"]'
    PERMISSION_ALLOW = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
    PERMISSION_DONT_ALLOW = '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'
    TAKE_PICTURE_ALLOW = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
    PHOTO = '//*[@resource-id="com.android.camera2:id/bottom_bar"]'
    ACCEPT_PHOTO = '//*[@resource-id="com.android.camera2:id/done_button"]'
    # CALENDAR
    YEAR = '//*[@resource-id="android:id/date_picker_header_year"]'
    PICK_YEAR = '//*[@text="2002"]'
    PICK_DAY = '//*[@text="19"]'


class Validation:
    # VALIDATION FORM
    TITLE = '//*[@resource-id="com.yapmap.yapmap:id/title_text_view"]'
    CODE_1 = '//*[@resource-id="com.yapmap.yapmap:id/first_code_edit_text"]'
    CODE_2 = '//*[@resource-id="com.yapmap.yapmap:id/second_code_edit_text"]'
    CODE_3 = '//*[@resource-id="com.yapmap.yapmap:id/third_code_edit_text"]'
    CODE_4 = '//*[@resource-id="com.yapmap.yapmap:id/fourth_code_edit_text"]'
    DESCRIPTION = '//*[@resource-id="com.yapmap.yapmap:id/validation_hint_text_view"]'
    RESEND = '//*[@resource-id="com.yapmap.yapmap:id/resend_code_button"]'


class Authorization:
    EMAIL = '//*[@resource-id="com.yapmap.yapmap:id/email_edit_text"]'
    PASSWORD = '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text"]'
    SIGNIN = '//*[@resource-id="com.yapmap.yapmap:id/sign_in_button"]'
