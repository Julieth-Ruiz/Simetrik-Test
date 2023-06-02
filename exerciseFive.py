#Get the text of the <h2> element
h2_element = driver.find_element(By.CSS_SELECTOR, "h2")
h2_text = h2_element.text
print("Texto de <h2>: " + h2_text)


# Get the text of the <p> element
p_element = driver.find_element(By.CSS_SELECTOR, "p")
p_text = p_element.text
print("Texto de <p>: " + p_text)    