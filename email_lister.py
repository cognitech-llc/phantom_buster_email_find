import pandas as pd


personal_folks = ['shoko@secondgenome.com','janet_adams@agilent.com',
'kaminker.josh@gene.com','m.sternberg@imperial.ac.uk']

avoid_list = ['vermeulen.rebecca@gene.com','jiang.zhaoshi@gilead.com',
'r.silva@surrey.ac.uk','wayne.visser@antwerpmanagementschool.be']

# Add CSV outputs of marketing campaigns already sent out
first_25_list = pd.read_csv('data_files/hubspot_campaigns/hubspot-crm-exports-first_test_list-2019-08-19.csv')
next_25_list = pd.read_csv('data_files/hubspot_campaigns/hubspot-crm-exports-next_25_emails-2019-08-19.csv')
next_100_list = pd.read_csv('data_files/hubspot_campaigns/hubspot-crm-exports-next_100_emails-2019-08-19.csv')
alllist = pd.read_csv('data_files/full_hubspot_extracts/hubspot-crm-exports-all-contacts-2019-10-01.csv')
gsheet = pd.read_csv('data_files/previous_manual_campaigns/HubSpot_List_GSheet.csv')
amazonworkmail = pd.read_csv('data_files/previous_manual_campaigns/AmazonWorkMail.csv')

# Get list of emails from HubSpot initial 3 lists, Gsheet and Amazon WorkMail
l1 = first_25_list['Email'].tolist()
l2 = next_25_list['Email'].tolist()
l3 = next_100_list['Email'].tolist()
gsheetemails = gsheet['Email'].tolist() + gsheet['Work email'].tolist()
amazon_list = amazonworkmail['Email'].tolist()

# Mega list of emails to filter
emails_to_filter = l1+l2+gsheetemails+amazon_list+personal_folks+avoid_list

# Filter NAs
filt_all_df =\
alllist[alllist['Email'].notnull()]

# Filter certain domains
filt_all_df =\
filt_all_df[~filt_all_df['Email'].\
str.contains('invalid.com|hubspot.com|cognitech-llc.com|gmail.com|yahoo.com|slideshare.net|.edu')]

# Filter out folks that are in the previous lists
filt_all_df =\
filt_all_df[~filt_all_df['Email'].isin(emails_to_filter)]

print (filt_all_df.shape)
filt_all_df['Email'].to_csv('data_files/contacts_to_email/All_Emails_Cleaned_10012019.CSV')
