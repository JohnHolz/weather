import * as React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

export default function Footer() {
  return (
    <Box
      component="footer"
      sx={{
        py: 2,
        px: 1,
        mt: "auto",
        color: "white",
        backgroundColor: "#747d8c",
      }}
    >
      <Container
        maxWidth="sm"
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-end",
        }}
      >
        <Box>
          <Typography variant="body1">EL</Typography>
        </Box>
        <Box>
          <Typography variant="body1">© 2022</Typography>
        </Box>
      </Container>
    </Box>
  );
}
