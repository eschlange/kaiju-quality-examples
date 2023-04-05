"""Just a place to quickly test some of the methods we've built"""

from Python.utilities.main_utils import BrowserSettings as Bs
from Python.utilities.main_utils import Elements, ElementType
from Python.utilities.main_utils import Interact as Inp

# TODO: REMOVE THIS FILE ONCE WE START BUILDING POMS, BUILDER CLASSES, AND ACTUAL TESTS - malexadner 4/5/2023
def main():
    driver = Bs.set_browser("chrome")
    Bs.navigate_to_url(driver, "https://www.google.com/")

    search_bar = Elements(ElementType.NAME, "q", "Google Search Input")
    search_button = Elements(ElementType.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]",
                             "Search Button")
    image_search_result_banner = Elements(ElementType.XPATH,
                                          "//*[@id='rso']/div[2]/div/div/div[2]/g-section-with-header/div[1]/title-with-lhs-icon/a/div[3]/h3",
                                          "Search Results Image Banner")

    Inp.input_text(driver, search_bar, "test pyramid")
    Inp.click_element(driver, search_button)

    actual_text = Inp.get_text(driver, image_search_result_banner)
    expected_text = "Images for test pyramid"

    if expected_text == actual_text:
        print("Text matches! :)")
        print("{0} == {1}".format(expected_text, actual_text))
        assert True
    else:
        try:
            assert False
        except AssertionError as err:
            print("Text did not match. :(")
            print("{0} != {1}".format(expected_text, actual_text))


if __name__ == "__main__":
    main()
