def generate_emails(input_file, output_file, keep_original_address_in_list):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            email = line.strip()
            if '@' in email:
                username, domain = email.split('@')
                new_email1 = f"{username}.e1@{domain}"
                new_email2 = f"{username}.e2@{domain}"
                if keep_original_address_in_list:
                    outfile.write(f"{email}\n")
                outfile.write(f"{new_email1}\n")
                outfile.write(f"{new_email2}\n")

# Example
input_filename = '/mnt/c/daten/temp/schule/input_emails.txt'  # File with email addresses as input
output_filename = '/mnt/c/daten/temp/schule/output_emails.txt'  # File to write the email addresses 

generate_emails(input_filename, output_filename, True)
