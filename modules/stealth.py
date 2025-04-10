import time
import random
from selenium.webdriver.common.action_chains import ActionChains

def random_delay(min_sec=2.0, max_sec=5.0):
    """
    Sleep for a random duration between min_sec and max_sec.
    """
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def human_like_mouse_move(browser, element):
    """
    Move the mouse smoothly to the element before clicking.
    """
    actions = ActionChains(browser)
    actions.move_to_element(element).pause(random.uniform(0.1, 0.3)).perform()

def smooth_scroll(browser, target_position, step=100, delay=0.05):
    """
    Scroll smoothly to a vertical position.
    """
    current_pos = browser.execute_script("return window.pageYOffset;")
    while abs(current_pos - target_position) > step:
        if current_pos < target_position:
            current_pos += step
        else:
            current_pos -= step
        browser.execute_script(f"window.scrollTo(0, {current_pos});")
        time.sleep(delay)
    browser.execute_script(f"window.scrollTo(0, {target_position});")

def limit_applications(max_per_session, cooldown_sec):
    """
    Generator to limit number of applications per session.
    """
    count = 0
    while True:
        if count >= max_per_session:
            print(f"Reached {max_per_session} applications, cooling down for {cooldown_sec} seconds.")
            time.sleep(cooldown_sec)
            count = 0
        yield count
        count += 1

def configure_stealth_browser(options):
    """
    Add stealth options to Selenium ChromeOptions.
    """
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Optionally set a real User-Agent string
    # options.add_argument("user-agent=YourRealUserAgentString")
    return options