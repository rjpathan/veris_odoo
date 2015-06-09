from openerp.osv import osv, fields

class veris_incident(osv.osv):
	_name = "veris.incident"

	_rec_name = "incident_id"

	_description = "VERIS (Vocabulary for Event Recording and Incident Sharing)"

	_columns = {
		'schema_version': fields.char('Schema Version'),
		'step': fields.selection([('Step1', 'Step1'), ('Step2', 'Step2'), ('Step3', 'Step3'), ('Step4', 'Step4'), ('Step5', 'Step5')], 'Step'),
		'progress': fields.float('Progress'),


		#incident:
		'incident_id': fields.char('Incident ID'),
		'source_id': fields.char('Source ID'),
		'security_incident': fields.selection([('Confirmed', 'Confirmed'), 
												('Suspected', 'Suspected'),
												('False positive', 'False positive'),
												('Near miss', 'Near miss')], 'Confirmed Incident?'),
		'summary': fields.text('Incident Summary', help='A brief summary of the incident.'),
		'confidence': fields.selection([('High','High'), ('Medium','Medium'),('Low','Low'),('None','None')], 
					'How certain are you that the information you provided about this incident is accurate?'),
		'notes': fields.text('Other Notes/Instructions'),

		#timeline:
		'incident_date': fields.date('When did the Incident Occur?'),
		'timeline_years': fields.char('Incident Year', size=4),
		'timeline_months': fields.char('Incident Month', size=2),
		'timeline_days': fields.char('Incident Day', size=2),



		#timelines:
		'timeline_unit_compromise': fields.selection([('NA', 'Not Applicable'), ('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Years', 'Years'), ('Never', 'Never'), ('Unknown', 'Unknown')], 'Time to Compromise'),
		'timeline_unit_exfiltration': fields.selection([('NA', 'Not Applicable'), ('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Years', 'Years'), ('Never', 'Never'), ('Unknown', 'Unknown')], 'Time to Exfiltration'),
		'timeline_unit_discovery': fields.selection([('NA', 'Not Applicable'), ('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Years', 'Years'), ('Never', 'Never'), ('Unknown', 'Unknown')], 'Time to Discovery'),
		'timeline_unit_exfiltration': fields.selection([('NA', 'Not Applicable'), ('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Years', 'Years'), ('Never', 'Never'), ('Unknown', 'Unknown')], 'Time to Exfiltration'),
		'timeline_unit_containment': fields.selection([('NA', 'Not Applicable'), ('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Years', 'Years'), ('Never', 'Never'), ('Unknown', 'Unknown')], 'Time to Containment'),
		'time_compromise': fields.float('Time to Compromise'),
		'time_exfiltration': fields.float('Time to Exfiltration'),
		'time_discovery': fields.float('Time to Discovery'),
		'time_containment': fields.float('Time to Containment'),

		'discovery_method': fields.selection([('Ext - actor disclosure', 'External - actor disclosure'), ('Ext - fraud detection', 'External - fraud detection'), ('Ext - monitoring service', 'External - monitoring service'), ('Ext - customer', 'External - customer'), ('Ext - audit', 'External - audit'), ('Ext - law enforcement', 'External - law enforcement'), ('Ext - incident response', 'External - incident response'), ('Ext - found documents', 'External - found documents'), ('Ext - suspicious traffic', 'External - suspicious traffic'), ('Ext - emergency response team', 'External - emergency response team'), ('Ext - unknown', 'External - unknown'), ('Int - antivirus', 'Internal - antivirus'), ('Int - incident response', 'Internal - incident response'), ('Int - infrastructure monitoring', 'Internal - infrastructure monitoring'), ('Int - financial audit', 'Internal - financial audit'), ('Int - fraud detection', 'Internal - fraud detection'), ('Int - HIDS', 'Internal - HIDS'), ('Int - IT review', 'Internal - IT review'), ('Int - log review', 'Internal - log review'), ('Int - NIDS', 'Internal - NIDS'), ('Int - security alarm', 'Internal - security alarm'), ('Int - reported by employee', 'Internal - reported by employee'), ('Int - data loss prevention', 'Internal - data loss prevention'), ('Int - unknown', 'Internal - unknown'), ('Prt - monitoring service', 'Private - monitoring service'), ('Prt - audit', 'Private - audit'), ('Prt - antivirus', 'Private - antivirus'), ('Prt - incident response', 'Private - incident response'), ('Prt - Unknown', 'Private - Unknown'), ('Prt - Other', 'Private - Other'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'How was the incident discovered?'),
		'discovery_note': fields.text('Other Notes'),


		'victim_ids': fields.one2many('veris.victim', 'incident_id', 'Victim Demographics'),
		'actor_ids': fields.one2many('veris.actor', 'incident_id', 'Actors'),
		'action_ids': fields.one2many('veris.action', 'incident_id', 'Actions'),
		'attribute_ids': fields.one2many('veris.attribute', 'incident_id', 'Attributes'),
		'asset_ids': fields.one2many('veris.asset', 'incident_id', 'Assets'),
		'impact_ids': fields.one2many('veris.impact', 'incident_id', 'Impact'),
	}

	_defaults = {
		'schema_version' : '1.3',
		'step': 'Step1',
		'progress': 10.0,
	}

	def create(self, cr, uid, vals, context=None):
		incident_seq = self.pool.get('ir.sequence').get(cr, uid, 'veris.incident') or '/'
		vals['incident_id'] = incident_seq
		return super(veris, self).create(cr, uid, vals, context)

	def next(self, cr, uid, ids, context=None):
		for rec in self.browse(cr, uid, ids):
			if rec.step == 'Step1':
				return self.write(cr, uid, ids, {'step': 'Step2', 'progress': 33.0})
			elif rec.step == 'Step2':
				return self.write(cr, uid, ids, {'step': 'Step3', 'progress': 60.0})
			elif rec.step == 'Step3':
				return self.write(cr, uid, ids, {'step': 'Step4', 'progress': 80.0})
			elif rec.step == 'Step4':
				return self.write(cr, uid, ids, {'step': 'Step5', 'progress': 100.0})


	def previous(self, cr, uid, ids, context=None):
		for rec in self.browse(cr, uid, ids):
			if rec.step == 'Step2':
				return self.write(cr, uid, ids, {'step': 'Step1', 'progress': 10.0})
			elif rec.step == 'Step3':
				return self.write(cr, uid, ids, {'step': 'Step2', 'progress': 33.0})
			elif rec.step == 'Step4':
				return self.write(cr, uid, ids, {'step': 'Step3', 'progress': 60.0})
			elif rec.step == 'Step5':
				return self.write(cr, uid, ids, {'step': 'Step4', 'progress': 80.0})




class veris_victim(osv.osv):
	_name = "veris.victim"

	_columns = {
		'incident_id': fields.many2one('veris.incident', 'Incident ID'),
		#victim:
		'victim_industry': fields.selection(
									[
										('11', 'Agriculture, Forestry, Fishing and Hunting '), 
										('21', 'Mining '), 
										('22', ' Utilities '), 
										('23', 'Construction '), 
										('31-33', 'Manufacturing '), 
										('42', 'Wholesale Trade '), 
										('44-45', 'Retail Trade '), 
										('48-49', 'Transportation and Warehousing '), 
										('51', 'Information '), 
										('52', 'Finance and Insurance '), 
										('53', 'Real Estate Rental and Leasing '), 
										('54', 'Professional, Scientific, and Technical Services '), 
										('55', 'Management of Companies and Enterprises '), 
										('56', 'Administrative and Support and Waste Management and Remediation Services '), 
										('61', 'Educational Services '), 
										('62', 'Health Care and Social Assistance '), 
										('71', 'Arts, Entertainment, and Recreation '), 
										('72', 'Accommodation and Food Services '), 
										('81', 'Other Services (except Public Administration) '), 
										('92', 'Public Administration ')
									], 'Victim Industry'),
		'victim_country_id':fields.many2one('res.country', 'Country of Operation'),
		'victim_country': fields.related('victim_country_id', 'code', type='char', string='Victim Country Code', store=True),
		'victim_employee_count': fields.selection([('1 to 10', '1 to 10'), ('11 to 100', '11 to 100'), ('101 to 1000', '101 to 1000'), ('1001 to 10000', '1001 to 10000'), ('10001 to 25000', '10001 to 25000'), ('25001 to 50000', '25001 to 50000'), ('50001 to 100000', '50001 to 100000'), ('Over 100000', 'Over 100000'), ('Unknown', 'Unknown')], 'Number Of Employees in Organization'),
		'victim_notes': fields.text('Other Notes'),

	}


class veris_actor(osv.osv):
	_name = "veris.actor"

	_columns = {
		'incident_id': fields.many2one('veris.incident', 'Incident'),
		#actor:
		'actor_internal': fields.boolean('Internal'),
		'actor_external': fields.boolean('External'),
		'actor_partner': fields.boolean('Partner'),
		'actor_unknown': fields.boolean('Unknown'),
		
		'actor_external_variety': fields.selection([( "Activist", "Activist" ), ( "Auditor", "Auditor" ), ( "Competitor", "Competitor" ), ( "Customer", "Customer" ), ( "Force majeure", "Force majeure" ), ( "Former employee", "Former employee" ), ( "Nation-state", "Nation-state" ), ( "Organized crime", "Organized crime" ), ( "Acquaintance", "Acquaintance" ), ( "State-affiliated", "State-affiliated" ), ( "Terrorist", "Terrorist" ), ( "Unaffiliated", "Unaffiliated" ), ( "Unknown", "Unknown" ), ( "Other", "Other" )], 'Varieties of external actors'),
		'actor_internal_variety': fields.selection([( "Auditor", "Auditor" ), ( "Call center", "Call center" ), ( "Cashier", "Cashier" ), ( "End-user", "End-user" ), ( "Executive", "Executive" ), ( "Finance", "Finance" ), ( "Helpdesk", "Helpdesk" ), ( "Human resources", "Human resources" ), ( "Maintenance", "Maintenance" ), ( "Manager", "Manager" ), ( "Guard", "Guard" ), ( "Developer", "Developer" ), ( "System admin", "System admin" ), ( "Unknown", "Unknown" ), ( "Other", "Other" )], 'Varieties of Internal actors'),

		'actor_external_motive': fields.selection([( "NA", "NA", ), ( "Espionage", "Espionage", ), ( "Fear", "Fear", ), ( "Financial", "Financial", ), ( "Fun", "Fun", ), ( "Grudge", "Grudge", ), ( "Ideology", "Ideology", ), ( "Convenience", "Convenience", ), ( "Secondary", "Secondary", ), ( "Unknown", "Unknown", ), ( "Other", "Other" )], 'Motives of External Actors'),
		'actor_internal_motive': fields.selection([( "NA", "NA", ), ( "Espionage", "Espionage", ), ( "Fear", "Fear", ), ( "Financial", "Financial", ), ( "Fun", "Fun", ), ( "Grudge", "Grudge", ), ( "Ideology", "Ideology", ), ( "Convenience", "Convenience", ), ( "Secondary", "Secondary", ), ( "Unknown", "Unknown", ), ( "Other", "Other" )], 'Motives of Internal Actors'),
		'actor_partner_motive': fields.selection([( "NA", "NA", ), ( "Espionage", "Espionage", ), ( "Fear", "Fear", ), ( "Financial", "Financial", ), ( "Fun", "Fun", ), ( "Grudge", "Grudge", ), ( "Ideology", "Ideology", ), ( "Convenience", "Convenience", ), ( "Secondary", "Secondary", ), ( "Unknown", "Unknown", ), ( "Other", "Other" )], 'Motives of Partner'),

		'actor_external_origin_id': fields.many2one('res.country', 'Country/affiliation of external actors'),
		'actor_external_origin': fields.related('actor_external_origin_id', 'code', type='char', string='Country', store=True),

		'actor_external_notes': fields.text('Misc external actor notes'),
		'actor_internal_notes': fields.text('Misc internal actor notes'),
		'actor_partner_notes': fields.text('Misc Partner notes'),

		'actor_partner_industry': fields.selection(
										[
										('11', 'Agriculture, Forestry, Fishing and Hunting '), 
										('21', 'Mining '), 
										('22', ' Utilities '), 
										('23', 'Construction '), 
										('31-33', 'Manufacturing '), 
										('42', 'Wholesale Trade '), 
										('44-45', 'Retail Trade '), 
										('48-49', 'Transportation and Warehousing '), 
										('51', 'Information '), 
										('52', 'Finance and Insurance '), 
										('53', 'Real Estate Rental and Leasing '), 
										('54', 'Professional, Scientific, and Technical Services '), 
										('55', 'Management of Companies and Enterprises '), 
										('56', 'Administrative and Support and Waste Management and Remediation Services '), 
										('61', 'Educational Services '), 
										('62', 'Health Care and Social Assistance '), 
										('71', 'Arts, Entertainment, and Recreation '), 
										('72', 'Accommodation and Food Services '), 
										('81', 'Other Services (except Public Administration) '), 
										('92', 'Public Administration ')
									], 'Victim Industry'),
		'actor_partner_country_id': fields.many2one('res.country', 'Country of operation'),
		'actor_partner_country': fields.related('actor_partner_country_id', 'code', type='char', string='Country', store=True),
	}



class veris_action(osv.osv):
	_name = "veris.action"

	_columns = {
		'incident_id': fields.many2one('veris.incident', 'Incident'),
		#actions:
		'action_malware_check': fields.boolean('Malware'),
		'action_hacking_check': fields.boolean('Hacking'),
		'action_social_check': fields.boolean('Social'),
		'action_misuse_check': fields.boolean('Misuse'),
		'action_physical_check': fields.boolean('Physical'),
		'action_error_check': fields.boolean('Error'),
		'action_environmental_check': fields.boolean('Environmental'),
		'action_unknown_check': fields.boolean('Unknown'),

		'action_environmental_variety': fields.selection([( "Deterioration", "Deterioration" ), ( "Earthquake", "Earthquake" ), ( "EMI", "EMI" ), ( "ESD", "ESD", ), ( "Temperature", "Temperature" ), ( "Fire", "Fire" ), ( "Flood", "Flood" ), ( "Hazmat", "Hazmat" ), ( "Humidity", "Humidity" ), ( "Hurricane", "Hurricane" ), ( "Ice", "Ice" ), ( "Landslide", "Landslide" ), ( "Lightning", "Lightning" ), ( "Meteorite", "Meteorite" ), ( "Particulates", "Particulates" ), ( "Pathogen", "Pathogen" ), ( "Power failure", "Power failure" ), ( "Tornado", "Tornado" ), ( "Tsunami", "Tsunami" ), ( "Vermin", "Vermin" ), ( "Volcano", "Volcano" ), ( "Leak", "Leak" ), ( "Wind", "Wind" ), ( "Unknown", "Unknown" ), ( "Other", "Other" )], 'Varieties of environmental events'),
		'action_environmental_notes': fields.text('Misc Environmental Notes'),

		'action_malware_variety': fields.selection([( "Adware", "Adware" ), ( "Backdoor", "Backdoor" ), ( "Brute force", "Brute force" ), ( "Capture app data", "Capture app data" ), ( "Capture stored data", "Capture stored data" ), ( "Client-side attack", "Client-side attack" ), ( "Click fraud", "Click fraud" ), ( "C2", "C2" ), ( "Destroy data", "Destroy data" ), ( "Disable controls", "Disable controls" ), ( "DoS", "DoS" ), ( "Downloader", "Downloader" ), ( "Exploit vuln", "Exploit vuln" ), ( "Export data", "Export data" ), ( "Packet sniffer", "Packet sniffer" ), ( "Password dumper", "Password dumper" ), ( "Ram scraper", "Ram scraper" ), ( "Ransomware", "Ransomware" ), ( "Rootkit", "Rootkit" ), ( "Scan network", "Scan network" ), ( "Spam", "Spam" ), ( "Spyware/Keylogger", "Spyware/Keylogger" ), ( "SQL injection", "SQL injection" ), ( "Adminware", "Adminware" ), ( "Worm", "Worm" ), ( "Unknown", "Unknown" ), ( "Other", "Other" )], 'Varieties or functions of malware'),
		'action_malware_vector': fields.selection([('Direct install', 'Direct install'), ('Download by malware', 'Download by malware'), ('Email autoexecute', 'Email autoexecute'), ('Email link', 'Email link'), ('Email attachment', 'Email attachment'), ('Instant messaging', 'Instant messaging'), ('Network propagation', 'Network propagation'), ('Remote injection', 'Remote injection'), ('Removable media', 'Removable media'), ('Software update', 'Software update'), ('Web drive-by', 'Web drive-by'), ('Web download', 'Web download'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Vectors or paths of infection'),
		'action_malware_cve': fields.text('CVEs exploited by this malware'),
		'action_malware_name': fields.char('Common name or strain'),
		'action_malware_notes': fields.text('Misc Malware Notes'),

		'action_hacking_variety': fields.selection([('Abuse of functionality', 'Abuse of functionality'), ('Brute force', 'Brute force'), ('Buffer overflow', 'Buffer overflow'), ('Cache poisoning', 'Cache poisoning'), ('Session prediction', 'Session prediction'), ('CSRF', 'CSRF'), ('XSS', 'XSS'), ('Cryptanalysis', 'Cryptanalysis'), ('DoS', 'DoS'), ('Footprinting', 'Footprinting'), ('Forced browsing', 'Forced browsing'), ('Format string attack', 'Format string attack'), ('Fuzz testing', 'Fuzz testing'), ('HTTP request smuggling', 'HTTP request smuggling'), ('HTTP request splitting', 'HTTP request splitting'), ('HTTP response smuggling', 'HTTP response smuggling'), ('HTTP Response Splitting', 'HTTP Response Splitting'), ('Integer overflows', 'Integer overflows'), ('LDAP injection', 'LDAP injection'), ('Mail command injection', 'Mail command injection'), ('MitM', 'MitM'), ('Null byte injection', 'Null byte injection'), ('Offline cracking', 'Offline cracking'), ('OS commanding', 'OS commanding'), ('Pass-the-hash', 'Pass-the-hash'), ('Path traversal', 'Path traversal'), ('RFI', 'RFI'), ('Reverse engineering', 'Reverse engineering'), ('Routing detour', 'Routing detour'), ('Session fixation', 'Session fixation'), ('Session replay', 'Session replay'), ('Soap array abuse', 'Soap array abuse'), ('Special element injection', 'Special element injection'), ('SQLi', 'SQLi'), ('SSI injection', 'SSI injection'), ('URL redirector abuse', 'URL redirector abuse'), ('Use of backdoor or C2', 'Use of backdoor or C2'), ('Use of stolen creds', 'Use of stolen creds'), ('XML attribute blowup', 'XML attribute blowup'), ('XML entity expansion', 'XML entity expansion'), ('XML external entities', 'XML external entities'), ('XML injection', 'XML injection'), ('XPath injection', 'XPath injection'), ('XQuery injection', 'XQuery injection'), ('Virtual machine escape', 'Virtual machine escape'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties or methods of hacking'),
		'action_hacking_cve': fields.text('CVEs exploited through hacking'),
		'action_hacking_vector': fields.selection([('3rd party desktop', '3rd party desktop'), ('Backdoor or C2', 'Backdoor or C2'), ('Desktop sharing', 'Desktop sharing'), ('Physical access', 'Physical access'), ('Command shell', 'Command shell'), ('Partner', 'Partner'), ('VPN', 'VPN'), ('Web application', 'Web application'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Vectors or paths of attack'),
		'action_hacking_notes': fields.text('Misc hacking notes'),

		'action_social_variety': fields.selection([('Baiting', 'Baiting'), ('Bribery', 'Bribery'), ('Elicitation', 'Elicitation'), ('Extortion', 'Extortion'), ('Forgery', 'Forgery'), ('Influence', 'Influence'), ('Scam', 'Scam'), ('Phishing', 'Phishing'), ('Pretexting', 'Pretexting'), ('Propaganda', 'Propaganda'), ('Spam', 'Spam'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties of social tactics'),
		'action_social_vector': fields.selection([('Documents', 'Documents'), ('Email', 'Email'), ('In-person', 'In-person'), ('IM', 'IM'), ('Phone', 'Phone'), ('Removable media', 'Removable media'), ('SMS', 'SMS'), ('Social media', 'Social media'), ('Software', 'Software'), ('Website', 'Website'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Vectors of communication'),
		'action_social_target': fields.selection([('Auditor', 'Auditor'), ('Call center', 'Call center'), ('Cashier', 'Cashier'), ('Customer', 'Customer'), ('End-user', 'End-user'), ('Executive', 'Executive'), ('Finance', 'Finance'), ('Former employee', 'Former employee'), ('Helpdesk', 'Helpdesk'), ('Human resources', 'Human resources'), ('Maintenance', 'Maintenance'), ('Manager', 'Manager'), ('Partner', 'Partner'), ('Guard', 'Guard'), ('Developer', 'Developer'), ('System admin', 'System admin'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Target of social tactics'),
		'action_social_notes': fields.text('Misc social notes'),

		'action_misuse_variety': fields.selection([('Knowledge abuse', 'Knowledge abuse'), ('Privilege abuse', 'Privilege abuse'), ('Possession abuse', 'Possession abuse'), ('Data mishandling', 'Data mishandling'), ('Email misuse', 'Email misuse'), ('Net misuse', 'Net misuse'), ('Illicit content', 'Illicit content'), ('Unapproved workaround', 'Unapproved workaround'), ('Unapproved hardware', 'Unapproved hardware'), ('Unapproved software', 'Unapproved software'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties of misuse'),
		'action_misuse_vector': fields.selection([('Physical access', 'Physical access'), ('LAN access', 'LAN access'), ('Remote access', 'Remote access'), ('Non-corporate', 'Non-corporate'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Vectors or access methods'),
		'action_misuse_notes': fields.text('Misc Misuse notes'),
		
		'action_physical_variety': fields.selection([('Assault', 'Assault'), ('Bypassed controls', 'Bypassed controls'), ('Destruction', 'Destruction'), ('Disabled controls', 'Disabled controls'), ('Skimmer', 'Skimmer'), ('Snooping', 'Snooping'), ('Surveillance', 'Surveillance'), ('Tampering', 'Tampering'), ('Theft', 'Theft'), ('Wiretapping', 'Wiretapping'), ('Connection', 'Connection'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties of physical actions'),
		'action_physical_vector': fields.selection([('Partner facility', 'Partner facility'), ('Partner vehicle', 'Partner vehicle'), ('Personal residence', 'Personal residence'), ('Personal vehicle', 'Personal vehicle'), ('Public facility', 'Public facility'), ('Public vehicle', 'Public vehicle'), ('Victim secure area', 'Victim secure area'), ('Victim work area', 'Victim work area'), ('Victim public area', 'Victim public area'), ('Victim grounds', 'Victim grounds'), ('Visitor privileges', 'Visitor privileges'), ('Uncontrolled location', 'Uncontrolled location'), ('Privileged access', 'Privileged access'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Vector of physical access'),
		'action_physical_notes': fields.text('Misc Physical Notes'),

	
		'action_error_variety': fields.selection([('Classification error', 'Classification error'), ('Data entry error', 'Data entry error'), ('Disposal error', 'Disposal error'), ('Gaffe', 'Gaffe'), ('Loss', 'Loss'), ('Maintenance error', 'Maintenance error'), ('Misconfiguration', 'Misconfiguration'), ('Misdelivery', 'Misdelivery'), ('Misinformation', 'Misinformation'), ('Omission', 'Omission'), ('Physical accidents', 'Physical accidents'), ('Capacity shortage', 'Capacity shortage'), ('Programming error', 'Programming error'), ('Publishing error', 'Publishing error'), ('Malfunction', 'Malfunction'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties of errors'),
		'action_error_vector': fields.selection([('Random error', 'Random error'), ('Carelessness', 'Carelessness'), ('Inadequate personnel', 'Inadequate personnel'), ('Inadequate processes', 'Inadequate processes'), ('Inadequate technology', 'Inadequate technology'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Why errors occurred'),
		'action_error_notes': fields.text('Misc error notes'),
	}


class veris_asset(osv.osv):
	_name = "veris.asset"

	_columns = {
		'incident_id': fields.many2one('veris.incident', 'Incident'),
		#asset:
		'asset_variety': fields.selection([('S - Authentication', 'Authentication'), ('S - Backup', 'Backup'), ('S - Database', 'Database'), ('S - DHCP', 'DHCP'), ('S - Directory', 'Directory'), ('S - DCS', 'DCS'), ('S - DNS', 'DNS'), ('S - File', 'File'), ('S - Log', 'Log'), ('S - Mail', 'Mail'), ('S - Mainframe', 'Mainframe'), ('S - Payment switch', 'Payment switch'), ('S - POS controller', 'POS controller'), ('S - Print', 'Print'), ('S - Proxy', 'Proxy'), ('S - Remote access', 'Remote access'), ('S - SCADA', 'SCADA'), ('S - Web application', 'Web application'), ('S - Code repository', 'Code repository'), ('S - VM host', 'VM host'), ('S - Other', 'Other'), ('S - Unknown', 'Unknown'), ('N - Access reader', 'Access reader'), ('N - Camera', 'Camera'), ('N - Firewall', 'Firewall'), ('N - HSM', 'HSM'), ('N - IDS', 'IDS'), ('N - Broadband', 'Broadband'), ('N - PBX', 'PBX'), ('N - Private WAN', 'Private WAN'), ('N - PLC', 'PLC'), ('N - Public WAN', 'Public WAN'), ('N - RTU', 'RTU'), ('N - Router or switch', 'Router or switch'), ('N - SAN', 'SAN'), ('N - Telephone', 'Telephone'), ('N - VoIP adapter', 'VoIP adapter'), ('N - LAN', 'LAN'), ('N - WLAN', 'WLAN'), ('N - Other', 'Other'), ('U - Auth token', 'Auth token'), ('U - Desktop', 'Desktop'), ('U - Laptop', 'Laptop'), ('U - Media', 'Media'), ('U - Mobile phone', 'Mobile phone'), ('U - Peripheral', 'Peripheral'), ('U - POS terminal', 'POS terminal'), ('U - Tablet', 'Tablet'), ('U - Telephone', 'Telephone'), ('U - VoIP phone', 'VoIP phone'), ('U - Other', 'Other'), ('T - ATM', 'ATM'), ('T - PED pad', 'PED pad'), ('T - Gas terminal', 'Gas terminal'), ('T - Kiosk', 'Kiosk'), ('T - Other', 'Other'), ('M - Tapes', 'Tapes'), ('M - Disk media', 'Disk media'), ('M - Documents', 'Documents'), ('M - Flash drive', 'Flash drive'), ('M - Disk drive', 'Disk drive'), ('M - Smart card', 'Smart card'), ('M - Payment card', 'Payment card'), ('M - Other', 'Other'), ('P - System admin', 'System admin'), ('P - Auditor', 'Auditor'), ('P - Call center', 'Call center'), ('P - Cashier', 'Cashier'), ('P - Customer', 'Customer'), ('P - Developer', 'Developer'), ('P - End-user', 'End-user'), ('P - Executive', 'Executive'), ('P - Finance', 'Finance'), ('P - Former employee', 'Former employee'), ('P - Guard', 'Guard'), ('P - Helpdesk', 'Helpdesk'), ('P - Human resources', 'Human resources'), ('P - Maintenance', 'Maintenance'), ('P - Manager', 'Manager'), ('P - Partner', 'Partner'), ('P - Other', 'Other'), ('Unknown', 'Unknown')], 'What varieties of assets were compromised?'),
		'asset_ownership': fields.selection([('Customer', 'Customer'), ('Employee', 'Employee'), ('Partner', 'Partner'), ('Victim', 'Victim'), ('Unknown', 'Unknown'), ('NA', 'NA')], 'Who OWNS these asset(s)?'),
		'asset_hosting': fields.selection([('External', 'External'), ('External dedicated', 'External dedicated'), ('External shared', 'External shared'), ('Internal', 'Internal'), ('NA', 'NA'), ('Unknown', 'Unknown')], 'Who HOSTS (or stores) these asset(s)?'),
		'asset_management': fields.selection([('External', 'Externally managed'), ('Internal', 'Internally managed'), ('NA', 'NA'), ('Unknown', 'Unknown')], 'Who MANAGES these asset(s)?'),
		'asset_accessibility': fields.selection([('External', 'Publicly Accessible'), ('Internal', 'Internally Accessible'), ('Isolated', 'Internally Isolated or Restricted Environment'), ('NA', 'NA'), ('Unknown', 'Unknown')], 'Network ACCESSIBILITY of these asset(s)'),
		'asset_cloud': fields.selection([('Hypervisor', 'Hypervisor break-out attack'), ('Partner application', 'Application vulnerability in partner-developed application'), ('Hosting governance', 'Lack of security process or procedure by hosting provider'), ('Customer attack', 'Penetration of another web site on shared device'), ('Hosting error', 'Misconfiguration or error by hosting provider'), ('User breakout', 'Elevation of privilege by another customer in shared environment'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'If hosted "in the CLOUD," was this a contributing factor to the incident?'),
		'asset_note': fields.text('Misc Asset Notes'),
	}


class veris_attribute(osv.osv):
	_name = "veris.attribute"

	_columns = {
		'incident_id': fields.many2one('veris.incident', 'Incident'),
		#attributes:
		'attribute_confidentiality_check': fields.boolean('Confidentiality/Possession'),
		'attribute_integrity_check': fields.boolean('Integrity/Authenticity'),
		'attribute_availability_check': fields.boolean('Availability/Utility'),

		'attribute_confidentiality_data_disclosure': fields.selection([('Yes', 'Yes'), ('Potentially', 'Potentially (at risk)'), ('No', 'No'), ('Unknown', 'Unknown')], 'Was data disclosed?'),
		'attribute_confidentiality_state': fields.selection([('Stored', 'Stored'), ('Stored encrypted', 'Stored encrypted'), ('Stored unencrypted', 'Stored unencrypted'), ('Transmitted', 'Transmitted'), ('Transmitted encrypted', 'Transmitted encrypted'), ('Transmitted unencrypted', 'Transmitted unencrypted'), ('Processed', 'Processed'), ('Unknown', 'Unknown')], 'Data State'),
		'attribute_confidentiality_variety': fields.selection([('Credentials', 'Authentication Credentials (e.g. passwords, OTPs, biometrics)'), ('Bank', 'Bank Account Data'), ('Classified', 'Classified Information'), ('Copyrighted', 'Copyrighted material'), ('Digital certificate', 'Digital certificate'), ('Medical', 'Medical records'), ('Payment', 'Payment Card Data (e.g., PAN, PIN, CVV2, Expiration)'), ('Personal', 'Personal or identifying information (e.g., addr, ID#, credit score)'), ('Internal', 'Sensitive internal data (e.g., plans, reports, emails)'), ('Source code', 'Source code'), ('System', 'System information (e.g., config info, open services)'), ('Secrets', 'Trade Secrets'), ('Virtual currency', 'Virtual currency'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties (and amount) of data compromised'),
		'attribute_confidentiality_variety_data': fields.char('Amount of Data'),
		'attribute_confidentiality_notes': fields.text('Notes regarding Confidentiality/Possession loss'),

		'attribute_integrity_variety': fields.selection([('Created account', 'Created account'), ('Defacement', 'Defacement'), ('Hardware tampering', 'Hardware tampering'), ('Alter behavior', 'Alter behavior'), ('Fraudulent transaction', 'Fraudulent transaction'), ('Log tampering', 'Log tampering'), ('Repurpose', 'Repurpose'), ('Misrepresentation', 'Misrepresentation'), ('Modify configuration', 'Modify configuration'), ('Modify privileges', 'Modify privileges'), ('Modify data', 'Modify data'), ('Software installation', 'Software installation'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Varieties or nature of integrity loss'),
		'attribute_integrity_notes': fields.text('Misc integrity notes'),

		'attribute_availability_variety': fields.selection([('Destruction', 'Destruction'), ('Loss', 'Loss'), ('Interruption', 'Interruption'), ('Degradation', 'Degradation'), ('Acceleration', 'Acceleration'), ('Obscuration', 'Obscuration'), ('Unknown', 'Unknown'), ('Other', 'Other')], 'Variety or nature of availability loss'),
		'attribute_availability_notes': fields.text('Misc availability notes'),
	}


class veris_impact(osv.osv):
	_name = "veris.impact"

	_columns = {
		'incident_id': fields.many2one('veris.incident', 'Incident'),
		#impact (loss):
		'impact_overall': fields.float('Overall Impact'),
		'impact_asset_fraud': fields.float('Asset and fraud-related losses'),
		'impact_brand_market_damage': fields.float('Brand and market damage'),
		'impact_business_disruption': fields.float('Business disruption'),
		'impact_operating_costs': fields.float('Increased operating costs'),
		'impact_legal_regulatory_costs': fields.float('Legal and regulatory costs'),
		'impact_competitive_advantage_loss': fields.float('Loss of competitive advantage'),
		'impact_response_recovery_costs': fields.float('Response and recovery costs'),
		'impact_other': fields.float('Other'),

		'impact_overall_note': fields.text('Overall Impact'),
		'impact_asset_fraud_note': fields.text('Asset and fraud-related losses'),
		'impact_brand_market_damage_note': fields.text('Brand and market damage'),
		'impact_business_disruption_note': fields.text('Business disruption'),
		'impact_operating_costs_note': fields.text('Increased operating costs'),
		'impact_legal_regulatory_costs_note': fields.text('Legal and regulatory costs'),
		'impact_competitive_advantage_loss_note': fields.text('Loss of competitive advantage'),
		'impact_response_recovery_costs_note': fields.text('Response and recovery costs'),
		'impact_other_note': fields.text('Other'),
	}
