from django.db import models
from django.contrib.auth.models import User

import qrcode
from io import BytesIO
from django.core.files import File


# Create your models here.


class Application(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	id_no = models.IntegerField(max_length=10, default=100)
	qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
	accepted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	year_of_graduation = models.IntegerField()
	profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

	def __str__(self):
		return str(self.student.username) + ' - ' + str(self.id_no)

	def save(self, *args, **kwargs):
		if not self.pk:  # Only generate a QR code for new applications
			last_application = Application.objects.order_by('id_no').last()

			if last_application:
				# Convert id_no to a string before slicing to get the last 3 digits
				last_three_digits = int(str(last_application.id_no)[-3:])
				self.id_no = str(self.year_of_graduation)[2:] + str(last_three_digits + 1).zfill(3)
			else:
				# Default ID if no previous application exists
				self.id_no = str(self.year_of_graduation)[2:] + '100'

			# QR code generation logic remains the same
			qr = qrcode.QRCode(
				version=1,
				error_correction=qrcode.constants.ERROR_CORRECT_L,
				box_size=10,
				border=4,
			)
			qr.add_data(str(self.id_no))
			qr.make(fit=True)

			# Save the QR code as an image file
			img = qr.make_image(fill='black', back_color='white')
			img_io = BytesIO()
			img.save(img_io, format='PNG')

			img_file = File(img_io, name=f'{self.id_no}.png')
			self.qr_code.save(f'{self.id_no}.png', img_file, save=False)

		super().save(*args, **kwargs)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.URLField(max_length=200, blank=True, null=True)