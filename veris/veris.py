from openerp.osv import osv, fields

class veris(osv.osv):
	_name = "veris"

	_description = "VERIS (Vocabulary for Event Recording and Incident Sharing)"

	_columns = {
		'schema_version': fields.char('Schema Version'),
		'step': fields.selection([('Step1', 'Step1'), ('Step2', 'Step2'), ('Step3', 'Step3')], 'Step'),


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

	_defaults = {
		'schema_version' : '1.3',
		'step': 'Step1',
	}

	def create(self, cr, uid, vals, context=None):
		incident_seq = self.pool.get('ir.sequence').get(cr, uid, 'veris.incident') or '/'
		vals['incident_id'] = incident_seq
		return super(veris, self).create(cr, uid, vals, context)

	def next(self, cr, uid, ids, context=None):
		for rec in self.browse(cr, uid, ids):
			if rec.step == 'Step1':
				return self.write(cr, uid, ids, {'step': 'Step2'})
			elif rec.step == 'Step2':
				return self.write(cr, uid, ids, {'step': 'Step3'})

	def previous(self, cr, uid, ids, context=None):
		for rec in self.browse(cr, uid, ids):
			if rec.step == 'Step2':
				return self.write(cr, uid, ids, {'step': 'Step1'})
			elif rec.step == 'Step3':
				return self.write(cr, uid, ids, {'step': 'Step2'})


