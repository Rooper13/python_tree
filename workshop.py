def lrelu(z,alpha):
    fn=np.max(0.0*z,z)
    return(fn)