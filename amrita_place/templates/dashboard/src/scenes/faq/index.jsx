import { Box, useTheme } from "@mui/material";
import Header from "../../components/Header";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { tokens } from "../../theme";
import { useState, useEffect } from "react";

const FAQ = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [data, setdata] = useState([]);

// Using useEffect for single rendering
useEffect(() => {
    // Using fetch to fetch the api from 
    // flask server it will be redirected to proxy
    fetch("/dashboard/interviews").then((res) =>
        res.json().then((data) => {
            // Setting a data from api
            setdata(data);
        })
    );
}, []);
// console.log(data, data[0].positivePoints);
// var company = data[0].companyName;
// var positivePoints = data[0].positivePoints;
// var improve = data[0].improvements;
var company = "Google LLC";
var positivePoints = "Good start, managed ok with the technical questions";
var improve = "Must work on presentation skills";
  return (
    <Box m="20px">
      <Header title="INTERVIEW EXPERIENCE" subtitle="A list of student interview experiences" />

      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
          {company} - Interview Experience 
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Positive points: {positivePoints}. Scope for improvement: {improve}
          </Typography>
        </AccordionDetails>
      </Accordion>
      {/* <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            {data[0]['companyName']} Interview Experience
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Positive points: {data[0]['positivePoints']}. Scope for inprovement: {data[0]['improvements']}
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            {data[0]['companyName']} Interview Experience
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Positive points: {data[0]['positivePoints']}. Scope for inprovement: {data[0]['improvements']}
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            {data[0]['companyName']} Interview Experience
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Positive points: {data[0]['positivePoints']}. Scope for inprovement: {data[0]['improvements']}
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
        </Typography>
          <Typography color={colors.greenAccent[500]} variant="h5">
            {data[0]['companyName']} Interview Experience
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Positive points: {data[0]['positivePoints']}. Scope for inprovement: {data[0]['improvements']}
          </Typography>
        </AccordionDetails>
      </Accordion>


      {/* <Accordion defaultExpanded> */}
        {/* <AccordionSummary expandIcon={<ExpandMoreIcon />}> */}
          {/* <Typography color={colors.greenAccent[500]} variant="h5">
            Another Important Question
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            malesuada lacus ex, sit amet blandit leo lobortis eget.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            Your Favorite Question
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            malesuada lacus ex, sit amet blandit leo lobortis eget.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            Some Random Question
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography> */}
            {/* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse */}
            {/* malesuada lacus ex, sit amet blandit leo lobortis eget.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            The Final Question
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            malesuada lacus ex, sit amet blandit leo lobortis eget.
          </Typography>
        </AccordionDetails>
      </Accordion> */} 
    </Box>
  );
};

export default FAQ;
