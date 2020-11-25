from selenium import webdriver
import time


start_time = time.time()
def order():

    # Variables
    addToCart = '/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button/span/span'
    checkOut = 'html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]/span'
    signInEmail = '//*[@id="sign-in-email"]'
    signInPassword = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input'
    signInButton = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button'
    firstContinue = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span'
    secondContinue = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button/span'
    cvv = '//*[@id="cvv-confirm"]'
    reviewYourOrder = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button/span/span'


    # Keys
    myEmail = 'INSERT EMAIL HERE'
    myPassword = 'INSERT PASSWORD HERE'
    myCvv = 'INSERT CVV HERE'

    # Add to cart and checkout

    clickAddToCartButton(addToCart, driver)
    clickButton(checkOut, driver)


    # Sign in
    enterData(signInEmail, myEmail)
    enterData(signInPassword, myPassword)
    clickButton(signInButton, driver)

    # Continue to Review
    clickButton(firstContinue, driver)
    clickButton(secondContinue, driver)
    enterData(cvv, myCvv)
    clickButton(reviewYourOrder, driver)

    # Place order
    # clickButton(confirmOrder)

def clickButton(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(.8)
        clickButton(xpath, driver)

def enterData(field,data):
    try:
        driver.find_element_by_xpath(field).send_keys(data)
        pass
    except Exception:
        time.sleep(.8)
        enterData(field,data)

def clickAddToCartButton(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(.8)
        driver.refresh();
        clickAddToCartButton(xpath, driver)



if __name__ == "__main__":
    driver = webdriver.Firefox()
    #driver.get('https://www.walmart.com/ip/Sony-PlayStation-4-1TB-Slim-Gaming-Console/101507200')

    # Link for PS5 Digital Version; You can also put link for Xbox Series X or whatever
    driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815')
    time.sleep(.5)
    order()
    print("ordering")
    print("\nThe entire program took", time.time() - start_time, "seconds to run")
