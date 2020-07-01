class Locators:

    # Login page objects
    txtbox_username_xpath = "//input[@id='txtUsername']"
    txtbox_password_xpath = "//input[@id='txtPassword']"
    btn_login_xpath = "//input[@id='btnLogin']"
    span_invalid_info_xpath = "//span[@id='spanMessage']"

    # Home page objects
    btn_welcome_xpath = "//a[@id='welcome']"
    btn_logout_xpath = "//a[contains(text(),'Logout')]"
    span_leave_xpath = "//*[@id='menu_leave_viewLeaveModule']"
    span_assign_leave_xpath = "//span[contains(text(),'Assign Leave')]"

    # Leave page objects
    txt_emp_name_xpath = "//input[@id='assignleave_txtEmployee_empName']"
    ddl_leave_type_xpath = "//select[@id='assignleave_txtLeaveType']"
    date_pick_from_date_xpath = "//input[@id='assignleave_txtFromDate']"
    date_pick_to_date_xpath = "//input[@id='assignleave_txtToDate']"
    ddl_part_days_xpath = "//select[@id='assignleave_duration_duration']"
    txt_area_comment_xpath = "//textarea[@id='assignleave_txtComment']"
    btn_assign_xpath = "//input[@id='assignBtn']"
    btn_confirm_ok_xpath = "//input[@id='confirmOkButton']"