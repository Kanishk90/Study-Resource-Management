# Study-Resource-Management

About Project--> 
    Database 
        
            --user--
            id(pk)
            username(U)
            email(U)
            password
            activate
            fs_uniquefier
            Role_id(FK)

            --roles--
            id(pk,[stud,inst,admin])
            name
            description

            --Study Resources--
            id(pk)
            Topic
            Creator_id(Fk)
            youtube_link
            description
            likes
            is_approved

Requirements:- 
    1. There should be only one admin.
    2. Instructor should be approved by admin.
    3. Instructor has to approve study resources.
