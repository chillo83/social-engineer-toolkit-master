#!/usr/bin/env python
""" Python lists used for quick conversion of user input
    to strings used by the toolkit

    """

def encoder_type(encode):
    """
    Takes the value sent from the user encoding menu and returns
    the actual value to be used.

    """

    return {
            '0':"",
            '1':"shikata_ga_nai",
            '2':"",
            '3':"MULTIENCODE",
            '4':"BACKDOOR",
            }.get(encode,"ERROR")


def ms_module(exploit):
    """ Receives the input given by the user from gen_payload.py """

    return {
            '1':"exploit/windows/browser/ms14_012_textrange",
            '2':"exploit/windows/browser/ms14_012_cmarkup_uaf",
            '3':"exploit/windows/browser/ms13_080_cdisplaypointer",
            '4':"exploit/windows/browser/ie_setmousecapture_uaf",
            '5':"exploit/multi/browser/java_jre17_jmxbean_2",
            '6':"exploit/multi/browser/java_jre17_jmxbean",
            '7':"exploit/windows/browser/ms13_009_ie_slayoutrun_uaf",
            '8':"exploit/windows/browser/ie_cbutton_uaf",
            '9':"exploit/multi/browser/java_jre17_exec",
            '10':"exploit/windows/browser/ie_execcommand_uaf",
            '11':"exploit/multi/browser/java_atomicreferencearray",
            '12':"exploit/multi/browser/java_verifier_field_access",
            '13':"exploit/windows/browser/ms12_037_same_id",
            '14':"exploit/windows/browser/msxml_get_definition_code_exec",
            '15':"exploit/windows/browser/adobe_flash_rtmp",
            '16':"exploit/windows/browser/adobe_flash_mp4_cprt",
            '17':"exploit/windows/browser/ms12_004_midi",
            '18':"multi/browser/java_rhino\nset target 1",
            '19':"windows/browser/ms11_050_mshtml_cobjectelement",
            '20':"windows/browser/adobe_flashplayer_flash10o",
            '21':"windows/browser/cisco_anyconnect_exec",
            '22':"windows/browser/ms11_003_ie_css_import",
            '23':"windows/browser/wmi_admintools",
            '24':"windows/browser/ms10_090_ie_css_clip",
            '25':"windows/browser/java_codebase_trust",
            '26':"windows/browser/java_docbase_bof",
            '27':"windows/browser/webdav_dll_hijacker",
            '28':"windows/browser/adobe_flashplayer_avm",
            '29':"windows/browser/adobe_shockwave_rcsl_corruption",
            '30':"windows/browser/adobe_cooltype_sing",
            '31':"windows/browser/apple_quicktime_marshaled_punk",
            '32':"windows/browser/ms10_042_helpctr_xss_cmd_exec",
            '33':"windows/browser/ms10_018_ie_behaviors",
            '34':"windows/browser/ms10_002_aurora",
            '35':"windows/browser/ms10_018_ie_tabular_activex",
            '36':"windows/browser/ms09_002_memory_corruption",
            '37':"windows/browser/ms09_072_style_object",
            '38':"windows/browser/ie_iscomponentinstalled",
            '39':"windows/browser/ms08_078_xml_corruption",
            '40':"windows/browser/ie_unsafe_scripting",
            '41':"multi/browser/firefox_escape_retval",
            '42':"windows/browser/mozilla_mchannel",
            '43':"auxiliary/server/browser_autopwn",
           }.get(exploit,"ERROR")


# called from gen_payload.py
# uses payload_menu_2
def ms_payload(payload):
    """
    Receives the input given by the user from create_payload.py
    and create_payloads.py

    """

    return {
            '1':"windows/shell_reverse_tcp",
            '2':"windows/meterpreter/reverse_tcp",
            '3':"windows/vncinject/reverse_tcp",
            #'4':"windows/shell_bind_tcp",
            #'5':"windows/x64/shell_bind_tcp",
            '4':"windows/x64/shell_reverse_tcp",
            '5':"windows/x64/meterpreter/reverse_tcp",
            '6':"windows/meterpreter/reverse_tcp_allports",
            '7':"windows/meterpreter/reverse_https",
            '8':"windows/meterpreter/reverse_tcp_dns",
            '9':"windows/download_exec",
            }.get(payload,"ERROR")

# called from create_payloads.py

def ms_payload_2(payload):
    """ Receives the input given by the user from create_payloadS.py """

    return {
            '1':"shellcode/pyinject",
            '2':"shellcode/multipyinject",
            '3':"set/reverse_shell",
            '4':"set/reverse_shell",
            '5':"set/reverse_shell",
            '6':"shellcode/alphanum",
            }.get(payload,"ERROR")

def ms_payload_3(payload):
    """ Receives the input given by the user from create_payloadS.py """

    return {
            '1':"windows/shell_reverse_tcp",
            '2':"windows/meterpreter/reverse_tcp",
            '3':"windows/vncinject/reverse_tcp",
            '4':"windows/x64/shell_reverse_tcp",
            '5':"windows/x64/meterpreter/reverse_tcp",
            '6':"windows/x64/shell_bind_tcp",
            '7':"windows/meterpreter/reverse_https",
            }.get(payload,"ERROR")


# uses create_payloads_menu
def ms_attacks(exploit):
    """ Receives the input given by the user from create_payload.py """

    return {
            '1':"dll_hijacking",
            '2':"unc_embed",
            '3':"exploit/windows/fileformat/ms14_017_rtf",
            '4':"exploit/windows/fileformat/ms11_006_createsizeddibsection",
            '5':"exploit/windows/fileformat/ms10_087_rtf_pfragments_bof",
            '6':"exploit/windows/fileformat/adobe_flashplayer_button",
            '7':"exploit/windows/fileformat/adobe_cooltype_sing",
            '8':"exploit/windows/fileformat/adobe_flashplayer_newfunction",
            '9':"exploit/windows/fileformat/adobe_collectemailinfo",
            '10':"exploit/windows/fileformat/adobe_geticon",
            '11':"exploit/windows/fileformat/adobe_jbig2decode",
            '12':"exploit/windows/fileformat/adobe_pdf_embedded_exe",
            '13':"exploit/windows/fileformat/adobe_utilprintf",
            '14':"custom/exe/to/vba/payload",
            '15':"exploit/windows/fileformat/adobe_u3d_meshdecl",
            '16':'exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs',
            '17':"exploit/windows/fileformat/foxit_title_bof",
            '18':"exploit/windows/fileformat/apple_quicktime_pnsize",
            '19':"exploit/windows/fileformat/nuance_pdf_launch_overflow",
            '20':"exploit/windows/fileformat/adobe_reader_u3d",
            '21':"exploit/windows/fileformat/ms12_027_mscomctl_bof",
            }.get(exploit,"INVALID")

def teensy_config(choice):
    """ Receives the input given by the user from set.py """

    return {
            '1':"powershell_down.pde",
            '2':"wscript.pde",
            '3':"powershell_reverse.pde",
            '4':"beef.pde",
            '5':"java_applet.pde",
            '6':"gnome_wget.pde"
            }.get(choice,"ERROR")

def webattack_vector(attack_vector):
    """ Receives the input given by the user from set.py """

    return {
            '1':"java",
            '2':"browser",
            '3':"harvester",
            '4':"tabnapping",
            '5':"webjacking",
            '6':"multiattack",
            '7':"fsattack"
            }.get(attack_vector,"ERROR")


def category(category):
    """
    Takes the value sent from the user encoding menu and returns
    the actual value to be used.

    """

    return {
            '0':"0",
            '1':"phishing",
            '2':"webattack",
            '3':"infectious",
            '4':"payloads",
            '5':"mailer",
            '6':"arduino",
            '7':"sms",
            '8':"wireless",
            '9':"modules",
            '10':"cloner",
            '11':"harvester",
            '12':"tabnapping",
            '13':"teensy",
            '14':"binary2teensy",
            '15':"dll_hijacking",
            '16':"multiattack",
            '17':"java_applet",
            '18':"encoding",
            '19':"fasttrack",
            '20':"autopwn",
            '21':"mssql",
            '22':"scan",
            '23':"direct",
            '24':"exploits",
            '25':"active_target",
            '26':"shell",
            '27':"set",
            '28':"teensy2powershell",
            '29':"powershell",
            '30':"delldrac",
            '31':"ridenum",
            '32':"psexec",
            '33':"fsattack",
           }.get(category,"ERROR")
