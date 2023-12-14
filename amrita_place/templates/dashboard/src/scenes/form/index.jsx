import { Box, Button, TextField } from "@mui/material";
import { Formik } from "formik";
import * as yup from "yup";
import useMediaQuery from "@mui/material/useMediaQuery";
import Header from "../../components/Header";
import axios from'axios';

const Form = () => {
  const isNonMobile = useMediaQuery("(min-width:600px)");

  const createStudent = async (data) => {
    try {
      const response = await axios.post('/dashboard/create', data);
      if (response.status === 201) {
        console.log('Student created successfully!');
      } else {
        console.error('Error creating student:', response.data);
      }
    } catch (error) {
      console.error('Error creating student:', error);
    }
  };
  
  const handleFormSubmit = (values) => {
    createStudent(values);
    console.log(values);
  };

  return (
    <Box m="20px">
      <Header title="NEW STUDENT" subtitle="Create a New Student Profile" />

      <Formik
        onSubmit={handleFormSubmit}
        initialValues={initialValues}
        validationSchema={checkoutSchema}
      >
        {({
          values,
          errors,
          touched,
          handleBlur,
          handleChange,
          handleSubmit,
        }) => (
          <form onSubmit={handleSubmit}>
            <Box
              display="grid"
              gap="30px"
              gridTemplateColumns="repeat(4, minmax(0, 1fr))"
              sx={{
                "& > div": { gridColumn: isNonMobile ? undefined : "span 4" },
              }}
            >
              <TextField
  fullWidth
  variant="filled"
  type="text"
  label="Roll Number"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.roll_no}
  name="roll_no"
  error={!!touched.roll_no && !!errors.roll_no}
  helperText={touched.roll_no && errors.roll_no}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="text"
  label="Name"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.name}
  name="name"
  error={!!touched.name && !!errors.name}
  helperText={touched.name && errors.name}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="email"
  label="Email"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.email_id}
  name="email_id"
  error={!!touched.email_id && !!errors.email_id}
  helperText={touched.email_id && errors.email_id}
  sx={{ gridColumn: "span 4" }}
/>
<TextField
                fullWidth
                variant="filled"
                type="text"
                label="Contact Number"
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.phoneNumber}
                name="phoneNumber"
                error={!!touched.phoneNumber && !!errors.phoneNumber}
                helperText={touched.phoneNumber && errors.phoneNumber}
                sx={{ gridColumn: "span 4" }}
              />
<TextField
  fullWidth
  variant="filled"
  type="url"
  label="LinkedIn Profile"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.linkedIN_profile}
  name="linkedIN_profile"
  error={!!touched.linkedIN_profile && !!errors.linkedIN_profile}
  helperText={touched.linkedIN_profile && errors.linkedIN_profile}
  sx={{ gridColumn: "span 4" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="number"
  label="Salary"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.salary}
  name="salary"
  error={!!touched.salary && !!errors.salary}
  helperText={touched.salary && errors.salary}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="number"
  label="CGPA"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.CGPA}
  name="CGPA"
  error={!!touched.CGPA && !!errors.CGPA}
  helperText={touched.CGPA && errors.CGPA}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="number"
  label="Pass Out Year"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.pass_out_year}
  name="pass_out_year"
  error={!!touched.pass_out_year && !!errors.pass_out_year}
  helperText={touched.pass_out_year && errors.pass_out_year}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="number"
  label="Company ID"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.companyID}
  name="companyID"
  error={!!touched.companyID && !!errors.companyID}
  helperText={touched.companyID && errors.companyID}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="number"
  label="Admin ID"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.adminID}
  name="adminID"
  error={!!touched.adminID && !!errors.adminID}
  helperText={touched.adminID && errors.adminID}
  sx={{ gridColumn: "span 2" }}
/>
<TextField
  fullWidth
  variant="filled"
  type="text"
  label="Program ID"
  onBlur={handleBlur}
  onChange={handleChange}
  value={values.programID}
  name="programID"
  error={!!touched.adminID && !!errors.adminID}
  helperText={touched.adminID && errors.adminID}
  sx={{ gridColumn: "span 2" }}
/>

            </Box>
            <Box display="flex" justifyContent="end" mt="20px">
              <Button type="submit" color="secondary" variant="contained">
                Create New Student
              </Button>
            </Box>
          </form>
        )}
      </Formik>
    </Box>
  );
};

const phoneRegExp =
  /^((\+[1-9]{1,4}[ -]?)|(\([0-9]{2,3}\)[ -]?)|([0-9]{2,4})[ -]?)*?[0-9]{3,4}[ -]?[0-9]{3,4}$/;

  const checkoutSchema = yup.object().shape({
    roll_no: yup.string().required("required"),
    name: yup.string().required("required"),
    email_id: yup.string().email("invalid email").required("required"),
    linkedIN_profile: yup.string().url("invalid url").notRequired(),
    salary: yup.number().min(0).required("required"),
    CGPA: yup.number().min(0).max(10).required("required"),
    pass_out_year: yup.number().min(1970).max(new Date().getFullYear()).required("required"),
    companyID: yup.number().min(1).required("required"),
    adminID: yup.number().min(1).required("required"),
    programID: yup.string().required("required"),
    phoneNumber: yup
.string()
.matches(phoneRegExp, "Phone number is not valid")
.required("required"),
  });
  


const initialValues = {
  roll_no: "",
  name: "",
  email_id: "",
  linkedIN_profile: "",
  salary: 0,
  CGPA: 0,
  pass_out_year: 2023,
  companyID: 3,
  phoneNumber: '',
  adminID: 1,
  programID: "CSE1",
};


export default Form;
