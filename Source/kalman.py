import cv

# a simple wrapper for the OpenCV Kalman filter
class Kalman:
	def __init__(self, initial_val=[0], p_noise=[1e-2], m_noise=[1e-3], m_mat=[1], ecv=[1]):
		self.kalman = cv.CreateKalman( len(initial_val), len(initial_val), 0 )
		self.measurement = cv.CreateMat( len(initial_val), 1, cv.CV_32FC1 )
		self.prediction = None
		cv.Zero( self.measurement )
		cv.SetIdentity( self.kalman.measurement_matrix, cv.RealScalar(*m_mat) )
		cv.SetIdentity( self.kalman.process_noise_cov, cv.RealScalar(*p_noise) )
		cv.SetIdentity( self.kalman.measurement_noise_cov, cv.RealScalar(*m_noise) )
		cv.SetIdentity( self.kalman.error_cov_post, cv.RealScalar(*ecv))
		for v in initial_val:
		    self.kalman.state_post[initial_val.index(v), 0] = v
		    self.kalman.state_pre[initial_val.index(v), 0] = v

	def get_prediction(self):
		self.prediction = cv.KalmanPredict( self.kalman )
		return self.prediction
	
	def correct(self, *corrections):
	    if self.prediction:
	        self.measurement = self.prediction
	    for c in corrections:
	        self.measurement[corrections.index(c), 0] = c
		cv.KalmanCorrect( self.kalman,  self.measurement)

res = [640,480]
#NOTE: face length Kalman filtering is only used on the frontal faces that are detected
face = Kalman(initial_val=[res[0] / 2, res[1] / 2, 140])

