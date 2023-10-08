# Functionalities & Entities

* ***User Registration / Profile Management:*** there should be a Registration Page that allows you to log in with your LinkedIn account or, alternatively, creating a custom account. When registering, the following information has to be retrieved from LinkedIn or provided by the user. Everything but the Nickname should be modifiable after registration from a *Profile Management Page*.
    - *Mandatory Fields*
        - Nickname (Publish)
        - Password (Private & Encrypted)
        - Name (Private Until Disclosure)
        - Surname (Private Until Disclosure)
        - E-Mail (Private Until Disclosure)
        - Phone Number (Private Until Disclosure)
        - Role: Surfer / Project Creator / Project Contributor / Both (Public)
    - *Non-Mandatory Fields*
        - Photo (Public)
        - Video Presentation (Upload Form, MP4, Public)
        - Spoken Languages (List of Tags, Public)
        - Curriculum Vitae (Upload Form, PDF, Public)
        - Newsletter Subscription (Checkbox, Private)
        - LinkedIn Profile (Private Until Disclosure)
        - Preferred Communication: Chat / Phone / E-Mail (Public)
    - *Contributor-Tailored Fields*
        - Interests & Skills (List of Tags, Public)
    - *Creator-Tailored Fields*
        - ???
    
    Every user also has some non-editable information that are automatically assigned by the system based on tailor-made heuristics and algorithms or, alternatively, manually assigned by system administrators.
    
    - *Date of Registration:* it indicates the user registration date.
    - *Status:* it is a categorical variable indicating the trustworthiness of the user based on the information they shared with the system.
        - *Pending:* the user has signed up but did not verify their e-mail yet. 
        - *Confirmed:* the user confirmed their e-mail.
        - V*erified:* the user shared their LinkedIn profile, either by logging in with it or adding it to their account.
    - *Contributor Level:* it is a real number ranging from 0 to 5 that indicates the expertise of *contributors* based on *creators* feedbacks.
    - *Creator Level:* it is a real number ranging from 0 to 5 that indicates the expertise of *creators* based on *contributors* feedbacks and actual project results.
    - *Contributed Projects:* list of projects the user contributed in, with information about the state of the collaboration (*pending, ongoing, terminated*).
    - *Created Projects:* list of projects the user created.

- ***Project Publication:*** every user that selected ***contributor*** as their role can create a project from a *Project Submission Page.* For each project, it should be possible to specify the following information. Everything should be modifiable after publication.
    - *Mandatory Info*
        - *Title* (Public)
        - *Description* (Public)
        - *Start Date* (Public)
        - *End Date* (Public)
        - *Owner(s)* (List of Users, Public)
        - *Collaborators* (List of Users, Public)
        - *Keywords* (List of Tags, Public)
        - *Country* (Public)
        - *Language(s)* (List of Tags, Public)
        - *Type of Collaboration:* On-Site / Hybrid / Remote (Public)
        - *Status:* Not-Started, Ongoing, Completed, Expired (Public)
    - *Non-Mandatory*
        - *Official Website* (Public)
        - *Project Repository* (Public)
- ***Project Browsing / Ask Contribution:*** there should be a simple Project Browsing Page that is accessible even if you are not registered. When clicking on a project, the specific page gets opened with all the project’s details, and a user can decide to ask the owner(s) to contribute by sharing their info. The owner(s) will be notified by email, and they can review the user’s profile.
- ***Contributors Browsing / Ask Contribution:*** there should be a simple Contributor Browsing Page that is accessible only to registered and verified creators. When clicking on a user, the specific profile gets opened and the user can ask the contributor to collaborate on one of the projects they are owner of.
- ***Chat:*** there should be a way for users to communicate. Every conversation has some basic attributes.
    - *Users* (List of Users)
    - *Messages* (List of Messages with Timestamps)
- ***Recommendation:*** there should be a mechanism to match contributors and project owners, and notify them both by e-mail. Each *contributor* can click on a '*Find a Project*' button, and each *creator* can click on a '*Find a Contributor*' button.

