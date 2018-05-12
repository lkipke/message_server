CREATE TABLE Contacts
(
    userid int AUTO_INCREMENT,
    firstname varchar(40),
    lastname varchar(40),
    PRIMARY KEY (userid)
);

CREATE TABLE Messages
(
    sender int,
    recipient int,
    messageid int AUTO_INCREMENT,
    msg_body varchar(255),
    msg_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (messageid)
);

ALTER TABLE Message
ADD FOREIGN KEY (userid)
REFERENCES Person(userid);
