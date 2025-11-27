def parse_config(config_string, required_settings):
    if config_string[-1]!='>':
        return "Error: Incomplete configuration."
    else:
        my_list=list(config_string)
        my_list.pop(-1)
        my_str=''.join(my_list)
        my_str=my_str.split("--")
        new_list=[]
        for c in my_str:
            parsed_values=c.split("::")
            new_list.append(parsed_values)
        result=[]
        for char in required_settings:
            is_found=False
            for config_char in new_list:
                if config_char[0]==char:
                    result.append(config_char[1])
                    is_found=True
                    break
            if not is_found:
                return f"Error: Missing setting ['{char}']"


        return result
                    
    



#output
# ['GuestNet', 'Secret123', 'DHCP']
# Error: Missing settings: ['PASS']
# Error: Incomplete configuration.
# ['Localhost', '8080', '30']



conf1 = "SSID::GuestNet--PASS::Secret123--IP::DHCP>"
req1 = ["SSID", "PASS", "IP"]
print(parse_config(conf1, req1))

# Test Case 2: Valid config but missing a setting
conf2 = "SSID::HomeWifi--CHANNEL::6>"
req2 = ["SSID", "PASS"]
print(parse_config(conf2, req2))

# Test Case 3: Invalid format (missing end bracket)
conf3 = "SSID::Office--PASS::Admin"
req3 = ["SSID"]
print(parse_config(conf3, req3))

# Test Case 4: Different order
conf4 = "TIMEOUT::30--PORT::8080--HOST::Localhost>"
req4 = ["HOST", "PORT", "TIMEOUT"]
print(parse_config(conf4, req4))