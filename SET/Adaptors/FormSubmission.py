class FormSubmission:
    def __init__(self, url, form_data={}, submit_click=""):
        self.url = url
        self.form_data = form_data
        self.submit_click = submit_click

    def run(self, core):
        with core.wait_for_page_load():
            driver = core.getDriver()
            driver.get(self.url)
            for name in self.form_data:
                driver.find_element_by_xpath("//input[@name='" + name + "']").send_keys(
                    self.form_data[name]
                )
            driver.find_element_by_xpath(
                "//input[@name='" + self.submit_click + "']"
            ).click()
