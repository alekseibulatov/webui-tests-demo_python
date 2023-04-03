from selene import browser, have


def test_successful_login():
    browser.open_url('https://qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type('qagurubot@gmail.com')
    browser.element('.login-form [name=password]').type('qagurupassword').press_enter()

    browser.element('.main-header__login').click()

    browser.should(have.url_containing('cms/system/login'))
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
