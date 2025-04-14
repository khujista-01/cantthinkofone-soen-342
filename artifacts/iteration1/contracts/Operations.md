# Identification of System Operations and Operation Contracts

## **1. MakeAccount() - Client**
### **Operation Contracts**
**Pre-Conditions:**
- The client must not have an account in the system.
- The Clerk must approve the request for the client to have an account.

**Post-Conditions:**
- The client receives a confirmation message of account creation.
- The client has an active account and can proceed with making service requests.

---

## **2. ServiceRequest() - Client**
### **Operation Contracts**
**Pre-Conditions:**
- The client must have an approved and active account.
- The Client must be logged in to make the request.

**Post-Conditions:**
- The client can search for services and select one or multiple options.
- A confirmation message is returned to the client by the system.

---

## **3. AddAvailabilitySchedule(time, service) - Expert**
### **Operation Contracts**
**Pre-Conditions:**
- The Expert must be logged in with valid credentials.
- The Expert must search for available services.
- The Expert must select the type of service they wish to offer.
- The Expert must choose a time slot for the service.

**Post-Conditions:**
- The system stores the time slot and selected services.
- A confirmation message is returned to the Expert.

---

## **4. Read() - Expert & Client**
### **Operation Contracts**
**Pre-Conditions:**
- The Client/Expert must have an active account.
- The Client/Expert must be logged in with valid credentials.

**Post-Conditions:**
- The user can view the displayed auctions, objects of interest, auction schedules, etc.

---

## **5. find(id) - Expert & Client**
### **Operation Contracts**
**Pre-Conditions:**
- The `id` must be a valid identifier.
- The system must be operational and able to access client records.

**Post-Conditions:**
- If the `id` exists, the system returns the client's details (`id`, name, contact info).
- If the `id` does not exist, the system returns `"Not Exist"`.

---

## **6. LogIn(Name, Email, Password) - Clerk & Expert**
### **Operation Contracts**
**Pre-Conditions:**
- The Clerk/Expert must have an active and existing account.

**Post-Conditions:**
- If the credentials are **valid**, a **successful login message** is returned.
- If the credentials are **invalid**, an **ERROR and TRY AGAIN** message is returned.

---

## **7. LogIn(Username, Password) - Client**
### **Operation Contracts**
**Pre-Conditions:**
- The Client's account must have been approved upon sign-up.
- The Client's account must be active and existing.

**Post-Conditions:**
- If the account is **pending approval**, return **"Approval Pending"** and prompt the client to request approval again.
- If the account is **approved**:
  - **Valid credentials**: A **successful login message** is returned.
  - **Invalid credentials**: An **ERROR and TRY AGAIN** message is returned.

---

## **8. deleteAccount(id) - Expert & Client**
### **Operation Contracts**
**Pre-Conditions:**
- The `id` must correspond to an existing Expert or Client.
- The Administrator (Clerk) must have the necessary permissions.
- The system must be operational and able to modify records.

**Post-Conditions:**
- If the `id` exists:
  - The account is **permanently deleted**.
  - Any associated services, schedules, or permissions are **revoked**.
  - The system returns a **confirmation message**.
- If the `id` does not exist:
  - The system returns an **error message**.

---

## **9. updateInfo(name, contact_info) - Expert & Client**
### **Operation Contracts**
**Pre-Conditions:**
- The `id` of the client or expert must exist.
- The Clerk must have the necessary permissions.
- The new name and contact information must be valid.

**Post-Conditions:**
- If the `id` exists:
  - The **name and contact info are updated**.
  - The system sends a **confirmation message** to the Clerk.
- If the `id` does not exist:
  - The system returns an **error message**.

---

## **10. approvalRequest() - Client**
### **Operation Contracts**
**Pre-Conditions:**
- The client must have submitted a **valid signup request**.
- The client’s account must be in a **pending state**.
- The Clerk must have **approval permissions**.

**Post-Conditions:**
- If the **approval is granted**:
  - The client’s status is updated to **"Approved"**.
  - The system **notifies the clerk**.
- If the **request is invalid** or **already processed**:
  - The system returns an **error message**.

---
