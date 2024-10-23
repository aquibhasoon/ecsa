from django.db import models
from django.contrib.auth.models import User

import qrcode
from io import BytesIO
from django.core.files import File


# Create your models here.

class Application(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	student_id_no = models.IntegerField(default=100)
	qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
	accepted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	year_of_graduation = models.IntegerField()
	profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

	def __str__(self):
		return str(self.student.username) + ' - ' + str(self.student_id)

	def save(self, *args, **kwargs):
		if not self.pk:
			# QR code generation logic remains the same
			qr = qrcode.QRCode(
				version=1,
				error_correction=qrcode.constants.ERROR_CORRECT_L,
				box_size=10,
				border=4,
			)
			qr.add_data(str(self.student_id_no))
			qr.make(fit=True)

			# Save the QR code as an image file
			img = qr.make_image(fill='black', back_color='white')
			img_io = BytesIO()
			img.save(img_io, format='PNG')

			img_file = File(img_io, name=f'{self.student_id_no}.png')
			self.qr_code.save(f'{self.student_id_no}.png', img_file, save=False)

			super().save(*args, **kwargs)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.URLField(max_length=200, blank=True, null=True)
