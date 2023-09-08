# Success Path:

---

### Example 1:

#### CASE: Account creation and API sends success

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

**Ask a question**: Hello. I would like to create an account\
**Answer**: Sure, I can help you with that. Could you please provide me with the following information:

1. Type of account you want to open (Current or Savings)
2. Your name
3. Your address (street, city, postcode, country)
4. Your job name
   Ask a question: Anton Muler Am Stadtpark, 9, Vienna, Austria QA Developer

**Answer**: Great! Your account has been successfully opened. You now have a Current account with us. If you have any further questions or need
assistance, feel free to ask.

---

### Example 2:

#### CASE: Account creation and API sends failure

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

Ask a question: Hey. I want to open an account here\
**Answer**: Sure! I can help you with that. Can you please provide me with the following information:

1. Type of account you want to open (Current or Savings)
2. Your name
3. Your address (street, city, postcode, country)
4. Your job name

**Ask a question:** Abc Abc Abc Abc\
**Answer**: Thank you for providing your name. Can you please provide the remaining information:

1. Type of account you want to open (Current or Savings)
2. Your address (street, city, postcode, country)
3. Your job name

**Ask a question:** Savings Parkrin 10, 1010, Vienna, Austria Student\
**Answer:** I apologize, but it seems that there was an issue with opening your account. Please try again later or contact customer support for
further assistance.

---

### Example 3:

#### CASE: Block account and got failure from the API

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

**Ask a question:** I lost my card and I need to block it\
**Answer:** I'm sorry to hear that you lost your card. To block it, I need some information from you. Can you please provide me with the following
details:

1. Brand of the lost card (e.g. Visa, Mastercard, American Express)
2. Last 4 digits of the lost card
3. Expiration date of the lost card
4. Reason for blocking the card

Once I have this information, I will be able to assist you in blocking your card.

**Ask a question:** Mastercard 4567 08/28 Lost
**Answer:** I apologize, but I encountered an error while trying to block your card. Please try again later or contact your card issuer directly to
report the loss and request a card block. They will be able to assist you further in this matter.

---

### Example 4:

#### CASE: User asks about the app and wants to open an account after a few interactions

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

**Ask a question:** I want to know more about this app\
**Answer:** RaiPay is a mobile payment app that allows users to make quick and convenient payments using their smartphones. It is the successor to the
ELBA-pay app. The app offers various payment options, including smart payment, which allows users to pay amounts up to EUR 50 by simply holding their
smartphone (with an active display) near the payment terminal. For higher amounts, authorization is required. In addition to smart payment, there are
two other payment settings available: quick payment and manual authorization for every payment made through RaiPay.

RaiPay provides transaction details for each successful transaction, including the date, time, amount, and status. Users can filter transactions made
exclusively with RaiPay and distinguish between payments made with digital cards, online merchants (not supported by RaiPay), or ATM withdrawals.

To use RaiPay, you need a Raiffeisen account with a debit card or a Raiffeisen credit card. The app is available for Android devices (version 7 and
above) and iOS devices (version 12 and above). RaiPay can be used at any merchant where contactless card payments are accepted.

RaiPay supports all smartphone manufacturers without any restrictions for Android users. However, iOS users cannot use RaiPay for mobile payments and
should continue using Apple Pay.

You can install RaiPay on multiple phones by adding and activating the cards on each phone. The customer cards added on one phone will automatically
appear on the new phone. An internet connection (data or Wi-Fi) is required to establish a connection between RaiPay and the Mein ELBA app for loading
cards and making payments.

There are no costs associated with setting up or using RaiPay.

**Ask a question:** Oh, cool. Do I pay any fees to use it?\
**Answer:** No, there are no costs or fees associated with setting up or using RaiPay. It is free to download and use the app for making payments.

**Ask a question:** So, I want to create an account now\
**Answer:** Sure! I can help you with that. To create an account, I will need some information from you. Please provide the following details:

1. Type of account: Current or Savings
2. Your full name
3. Your address (street, city, postcode, country)
4. Your job name or occupation

Once I have this information, I can proceed with opening your account.

**Ask a question:** Sara Schneider Kagraner 123, 1220, Vienna, Austria Student\
**Answer:** Great! Your account has been successfully created. You now have a savings account with RaiPay. You can start using the app to make
payments and manage your finances. If you have any further questions or need assistance, feel free to ask.

---

### Example 5:

#### CASE: User asks about the app and how to download it

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

**Ask a question:** What is this app about?\
**Answer:** This app is called RaiPay and it is a mobile payment app that allows users to make quick and convenient payments using their smartphones.
It replaces the previous ELBA-pay app.
Ask a question: My card was stolen. What should I do?
Answer: If your physical card is lost or stolen, you should immediately contact the card blocking hotline or contact your Raiffeisen advisor. They
will help you block your physical card to prevent any misuse. If you have also added your digital debit card to RaiPay
Ask a question: How can I pay using this app?
Answer: To make payments using the RaiPay app, follow these steps:

1. Make sure you have a Raiffeisen account with a debit card or a Raiffeisen credit card.
2. Download and install the RaiPay app on your smartphone. It
   Ask a question: Where can I find this app?
   Answer: The context does not provide information on where to download and install the RaiPay app.
   Ask a question: What do I need to download this app?
   Answer: To download and use RaiPay, you will need the following:

- A Raiffeisen account with a debit card or Raiffeisen credit card.
- A smartphone with Android 7+ or iOS 12+.

Please note that iOS users cannot

**Ask a question:** I have an Android, what do I do?\
**Answer:** If you have an Android smartphone, you can download the RaiPay app from the Google Play Store. Make sure your Android version is at least
Android 7 or higher. Once you have downloaded the app, you can follow the instructions to set up and

**Ask a question:** My syster has an IOS, what she should do?\
**Answer:** If your sister has an iOS device, she will not be able to use RaiPay for mobile payments. She can continue to use Apple Pay for mobile
payments instead.

---

# Failure Path:

#### CASE: Chat did not find some information in the pdf

### Example 1:

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

**Ask a question:** What is this app about?\
**Answer:** This app is called RaiPay and it is a mobile payment app that allows users to make payments with their smartphones. It replaces the
previous ELBA-pay app. RaiPay can be used for contactless payments at stores and also offers P2P transactions, storing customer cards, and managing
digital merchant connections.

**Ask a question:** I'm afraid of using this app. Is this app safe?\
**Answer:** Yes, RaiPay is a safe app to use

**Ask a question:** My card just expried. What should I do?\
**Answer:** If your debit or credit card expires, you do not need to add or activate the card again in RaiPay. You just need to have used the new
physical card once before it expires. If the card is not renewed by the bank, it will no longer be available for mobile payments in RaiPay after the
expiration date.

**Ask a question:** Ah, cool. How do I get this app?\
**Answer:** The context does not provide information on how to download and install the app.

**Ask a question:** Ah, cool. How do I download the app?\
**Answer:** The provided context does not mention how to download the app.

**Ask a question:** Ah, cool. What do I need to have this app?\
**Answer:** To use the RaiPay app, you will need the following:

- A Raiffeisen bank account with a debit card or a Raiffeisen credit card.
- A smartphone with Android version 7 or higher, or iOS version 12 or higher. Please note that iOS users cannot use RaiPay for mobile payments, as
  Apple Pay is used instead.
  Ask a question:

----------------

### Example 2:

#### CASE: User says that lost his card but does not trigger the block_card function.

RaiPay QA bot is ready. How can I help you?\
Type 'exit' to quit.

**Ask a question:** Someone stole my card\
**Answer:** I'm sorry to hear that. It's important to take immediate action to protect your account and prevent any unauthorized transactions. Here's
what you can do:

1. Contact your bank or card issuer: Notify them about the stolen card and provide them with the necessary details such as the card brand, last 4
   digits, and expiration date. They will block the card to prevent any further use.

2. Monitor your account: Keep a close eye on your account activity to identify any unauthorized transactions. Report any suspicious activity to your
   bank or card issuer.

3. File a police report: Contact your local police department and file a report about the stolen card. This will help in case of any fraudulent
   activity.

4. Update your payment information: If you have any recurring payments or subscriptions linked to the stolen card, update the payment information with
   your new card or a different payment method.

Remember to always keep your card details secure and never share them with anyone.

**Ask a question:** Can I block my card here?\
**Answer:** I'm sorry, but as an AI language model, I don't have the capability to directly block your card. You will need to contact your bank or
card issuer to block your stolen card. They will have the necessary tools and procedures in place to assist you with blocking your card and taking
appropriate actions to protect your account.
