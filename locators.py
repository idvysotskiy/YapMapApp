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
    FIRST_NAME_ERROR = '//*[@resource-id="com.yapmap.yapmap:id/textinput_error"]'
    LAST_NAME_ERROR = '//*[@resource-id="com.yapmap.yapmap:id/textinput_error"]'
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
    CALENDAR_OK = '//*[@resource-id="android:id/button1"]'

    # STEP 3/4
    TITLE_STEP_3 = '//*[@resource-id="com.yapmap.yapmap:id/personal_info_text_view"]'
    DESCRIPTION_STEP_3 = '//*[@text="Used for filters for Dating feature. You can add it late to your Personal Profile"]'
    PRIVATE_PROFILE_TEXT = '//*[@text="Private profile"]'
    PRIVATE_SWITCH = '//*[@resource-id="com.yapmap.yapmap:id/switch_compat"]'
    DESCRIPTION_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/description_text_view"]'
    STATUS_TEXT = '//*[@text="Status"]'
    STATUS_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/status_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    STATUS_SELECTION_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/status_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
    ORIENTATION_TEXT = '//*[@text="Sexual orientation"]'
    ORIENTATION_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/sexual_orientation_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    ORIENTATION_SELECTION_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/sexual_orientation_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
    RELIGION_TEXT = '//*[@text="Religion"]'
    RELIGION_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/religion_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    RELIGION_SELECTION_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/religion_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
    ETHNOS_TEXT = '//*[@text="Ethnos"]'
    ETHNOS_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/ethnos_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    ETHNOS_SELECTION_TEXT = '//*[@resource-id="com.yapmap.yapmap:id/ethnos_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
    HEIGHT_TEXT = '//*[@text="Height"]'
    HEIGHT_ENTER = '//*[@resource-id="com.yapmap.yapmap:id/height_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]'
    HEIGHT_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/height_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    WEIGHT_TEXT = '//*[@text="Weight"]'
    WEIGHT_ENTER = '//*[@resource-id="com.yapmap.yapmap:id/weight_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]'
    WEIGHT_SELECT = '//*[@resource-id="com.yapmap.yapmap:id/weight_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'


class Status:
    TITLE = '//*[@text="Status"]'
    SINGLE_TEXT = '//*[@text="Single"]'
    SINGLE_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
    MARRIED_TEXT = '//*[@text="Married"]'
    MARRIED_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]'
    DIVORCED_TEXT = '//*[@text="Divorced"]'
    DIVORCED_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]'
    WIDOWED_TEXT = '//*[@text="Widowed"]'
    WIDOWED_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]'
    COMPLICATED_TEXT = '//*[@text="Complicated"]'
    COMPLICATED_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]'


class Orientation:
    HETERO_TEXT = '//*[@text="Hetero"]'
    HETERO_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
    HOMO_TEXT = '//*[@text="Homo"]'
    HOMO_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]'
    BI_TEXT = '//*[@text="Bi"]'
    BI_SELECT = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]'


class Religion:
    TITLE = '//*[@text="Religion"]'
    CHRISTIANITY = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
    ISLAM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]'
    ATHEIST = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]'
    HINDUISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]'
    BUDDHISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]'
    CHINESE_TRADITIONAL_RELIGION = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]'
    ETHNIC_RELIGION = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]'
    AFRICAN_TRADITIONAL_RELIGIONS = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[8]'
    SIKHISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[9]'
    SPIRITISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[10]'
    JUDAISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[11]'
    BAHAI = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[12]'
    JAINISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[13]'
    SHINTO = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[14]'
    CAO_DAI = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[15]'
    ZOROASTRIANISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[9]'
    TENRIKYO = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[10]'
    NEO_PAGANISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[11]'
    UNITARIAN_UNIVERSALISM = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[12]'
    RASTAFARI = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[13]'
    ESOTERIC = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[14]'
    OTHER = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[15]'


class Ethnos:
    TITLE = '//*[@text="Ethnos"]'
    EUROPEAN = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
    BLACK = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]'
    ASIAN = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]'
    AMERICAN_RED_RACE = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]'
    CAUCASIAN_RACE_WHITE_RACE = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]'
    MALAYAN_BROWN_RACE = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]'
    ETHIOPID_BLACK_RACE = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]'
    MONGOLIAN_YELLOW_RACE = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[8]'


class HeightAndWeight:
    SWITCH_TEXT_1 = '//*[@resource-id="com.yapmap.yapmap:id/switch_text_1"]'
    SWITCH_TEXT_2 = '//*[@resource-id="com.yapmap.yapmap:id/switch_text_2"]'
    SWITCH = '//*[@resource-id="com.yapmap.yapmap:id/switch_compat"]'
    DONE = '//*[@resource-id="com.yapmap.yapmap:id/done_button"]'
    TEXT_EDIT = '//*[@resource-id="com.yapmap.yapmap:id/edit_text_view"]'


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
