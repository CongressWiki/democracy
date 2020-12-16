# Database

## Tables

### bills

- id - (pkey) text
- created_at - timestamp
- updated_at - timestamp
- introduced_at - timestamp
- introduced_by_chamber - text
- status_at - timestamp
- status - text
- sponsor_id - (fkey:members) text <!-- index -->
- cosponsors - jsonb - [(fkey:members) string]
- chamber - text <!-- index -->
- congress - (fkey:congress) text <!-- index -->
- committees - jsonb - [(fkey:committees) string]
- subject - text <!-- index -->
- alt_subjects -  jsonb - [string]
- title - text <!-- index -->
- summary - text
- status - text

### bill_activity

- id - (pkey) text
- created_at - timestamp
- updated_at - timestamp
- status_at - timestamp
- status - text
- bill_id - (fkey:bills) text <!-- index -->
- type - text
- description - text

### amendments

- id - (pkey) text
- created_at - timestamp
- updated_at - timestamp
- introduced_at - timestamp
- status_at - timestamp
- status - text
- bill_id - (fkey:bills) text <!-- index -->
- amends_amendment_id - (fkey:amendments) text <!-- index -->
- treaty_id - (fkey:treaty) text <!-- index? -->
- sponsor_id - (fkey:members) text <!-- index? -->
- congress - (fkey:congress) text <!-- index? -->
- cosponsors - jsonb - [(fkey:members) string]
- chamber - text
- type - text
- committees - jsonb - [(fkey:committees) string]

### amendments_activity

- id - (pkey) text
- created_at - timestamp
- updated_at - timestamp
- acted_at - timestamp
- status_at - timestamp
- status - text
- amendment_id - (fkey:bills) text <!-- index -->
- type - text
- description - text

### treaty

- id - (pkey) text
- title - text <!-- index? -->
- description - text

### congress

- id - (pkey) text
- service_start_at - timestamp
- service_end_at - timestamp

### committees

- id - (pkey) text
- created_at - timestamp
- updated_at - timestamp
- name - text <!-- index? -->
- description - text

### members

- id - (pkey) text
- created_at - timestamp
- updated_at - timestamp
- preferred_name - text
- first_name - text
- last_name - text
- gender - text
- state - (enum:state) text <!-- index? -->
- image_url - text
- is_government_official - boolean
- party_id - (fkey:parties) text <!-- index -->

### elected_officials

- id - (pkey) text
- updated_at - timestamp
- service_start_at - timestamp
- service_end_at - timestamp
- status_at - timestamp
- status - text
- member_id - (fkey:members) text <!-- index -->
- party_id - (fkey:parties) text <!-- index -->
- state - (enum:state) text
- district - text
- position - text <!-- Senator/House representative/Justice/President --> <!-- index -->
- rank - text <!-- Junior/Senior/Whip/Leader --> <!-- index? -->
- terms_served - number
- terms_remaining - number
- active - boolean <!-- index? -->
- description - text

### votes

- id - (pkey) text
- created_at - timestamp
<!-- - updated_at # Real legislative members can't reverse a vote, so why should we?  -->
- bill_id - (fkey:bills) text <!-- index -->
- member_id - (fkey:members) text <!-- index -->
- decision - text

### parties

- id - text
- name - text
- description - text
- leader_id - (fkey:members) text <!-- index -->

## Enums

### decisions

- yay <!-- "Yay" -->
- nay <!-- "Nay" -->
- present <!--  -->
- not_present <!--  -->

### states

...
