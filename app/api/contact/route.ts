import { NextResponse } from "next/server";
import nodemailer from "nodemailer";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { name, email, division, message } = body;

    const transporter = nodemailer.createTransport({
      service: "gmail",
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_APP_PASSWORD,
      },
    });

    const mailOptions = {
      from: `"${name}" <${process.env.GMAIL_USER}>`,
      to: process.env.CONTACT_EMAIL,
      replyTo: email,
      subject: `New Inquiry from ${name} - ${division}`,
      text: `Name: ${name}\nEmail: ${email}\nDivision: ${division}\n\nMessage:\n${message}`,
    };

    await transporter.sendMail(mailOptions);
    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Error sending email:", error);
    return NextResponse.json({ success: false, error: "Failed to send email" }, { status: 500 });
  }
}
