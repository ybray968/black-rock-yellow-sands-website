"use client";

import { useState } from "react";
import Image from "next/image";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { Users, Briefcase, MapPin, Globe, CheckCircle2, FileText } from "lucide-react";
import { Turnstile } from "@marsidev/react-turnstile";

export default function CareersPage() {
  const [token, setToken] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [fileError, setFileError] = useState("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (file.type !== "application/pdf") {
        setFileError("Only PDF files are accepted.");
        e.target.value = "";
      } else if (file.size > 5 * 1024 * 1024) {
        setFileError("File size must be under 5MB.");
        e.target.value = "";
      } else {
        setFileError("");
      }
    }
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!token) {
      alert("Please complete the bot protection check.");
      return;
    }
    setIsSubmitting(true);
    
    try {
      const formData = new FormData();
      formData.append("name", (document.getElementById("name") as HTMLInputElement).value);
      formData.append("email", (document.getElementById("email") as HTMLInputElement).value);
      formData.append("position", (document.getElementById("position") as HTMLSelectElement).value);
      
      const fileInput = document.getElementById("cv") as HTMLInputElement;
      if (fileInput.files?.[0]) {
        formData.append("cv", fileInput.files[0]);
      }

      const response = await fetch("/api/careers", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        setSubmitted(true);
      } else {
        alert("Failed to send application. Please try again later.");
      }
    } catch (error) {
      console.error(error);
      alert("An error occurred. Please try again later.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="bg-offwhite flex flex-col min-h-screen">
      {/* 1. HERO SECTION */}
      <section className="relative w-full h-[50vh] min-h-[400px] flex items-center overflow-hidden bg-forest">
        <div className="absolute inset-0 z-0 hidden md:block">
          <Image
            src="/images/home_hero.png"
            alt="Careers Hero"
            fill
            priority
            className="object-cover object-[65%_center] md:object-center opacity-40 hover:opacity-60 transition-opacity duration-1000 grayscale"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-forest via-forest/80 to-transparent" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <StaggerContainer className="max-w-3xl">
            <StaggerItem direction="up" className="mb-6 flex items-center gap-3">
              <Users className="w-6 h-6 text-gold" />
              <span className="text-gold font-serif italic tracking-wide">
                Join Us
              </span>
            </StaggerItem>
            <StaggerItem direction="up" className="mb-6">
              <h1 className="text-5xl md:text-7xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-[0.9]">
                Careers
              </h1>
            </StaggerItem>
            <StaggerItem direction="up">
              <p className="text-offwhite/80 text-lg md:text-xl font-normal leading-relaxed max-w-xl text-balance">
                Operating with the highest ethical standards in a modern, accessible environment. Join our friendly and professional team of global experts.
              </p>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>

      {/* 2. OPENINGS & APPLICATION FORM */}
      <section className="py-24 md:py-32 relative z-10 bg-offwhite">
        <div className="container mx-auto px-4 md:px-8 grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-24">
          
          {/* Left: Job Postings & General Info */}
          <div className="lg:col-span-7 flex flex-col gap-16">
            
            {/* ICC Lawyer Opening */}
            <div>
              <AnimatedSection direction="up">
                <h2 className="text-3xl md:text-4xl font-serif font-bold text-forest mb-4">
                  Current Openings
                </h2>
                <div className="w-16 h-px bg-gold mb-12" />
              </AnimatedSection>
              
              <AnimatedSection direction="up" delay={0.1} className="bg-white border border-forest/10 p-8 md:p-10 rounded-sm shadow-xl shadow-forest/5 hover:border-gold/50 transition-colors group">
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
                  <h3 className="text-2xl font-serif font-bold text-forest group-hover:text-gold transition-colors">
                    International Chamber of Commerce (ICC) Rules Lawyer
                  </h3>
                  <span className="bg-forest/5 text-forest font-bold text-xs uppercase tracking-widest px-4 py-2 rounded-full whitespace-nowrap">
                    Active
                  </span>
                </div>
                
                <p className="text-forest/70 font-normal leading-relaxed mb-8">
                  We are seeking an expert legal professional specializing in International Chamber of Commerce (ICC) rules. 
                  The role focuses primarily on comprehensive contract creation, strategic evaluation, and international trade law.
                </p>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="flex items-center gap-3 text-forest/80 font-medium text-sm">
                    <Briefcase className="w-5 h-5 text-gold" />
                    <span>Full Time Position</span>
                  </div>
                  <div className="flex items-center gap-3 text-forest/80 font-medium text-sm">
                    <MapPin className="w-5 h-5 text-gold" />
                    <span>Muscat, Oman</span>
                  </div>
                  <div className="flex items-center gap-3 text-forest/80 font-medium text-sm md:col-span-2">
                    <Globe className="w-5 h-5 text-gold" />
                    <span>Bilingual Required (Arabic / English)</span>
                  </div>
                </div>
              </AnimatedSection>
            </div>

            {/* General Submission */}
            <AnimatedSection direction="up" delay={0.2} className="bg-forest text-offwhite p-10 rounded-sm border-l-4 border-gold relative overflow-hidden">
              <Users className="absolute -bottom-8 -right-8 w-48 h-48 text-offwhite/5 pointer-events-none" />
              <h3 className="text-2xl font-serif font-bold mb-4 relative z-10">
                Empower Our Team
              </h3>
              <p className="text-offwhite/80 font-normal leading-relaxed relative z-10 max-w-lg">
                If the position you are interested in is not currently open, but you feel like you can empower our team, then don't hesitate to contact us with your CV. We are always looking for exceptional talent to drive our vision forward.
              </p>
            </AnimatedSection>

          </div>

          {/* Right: Application Form */}
          <div className="lg:col-span-5 relative">
            <div className="sticky top-32">
              <AnimatedSection direction="left" delay={0.3} className="bg-white p-8 md:p-10 border border-forest/10 rounded-sm shadow-xl shadow-forest/5">
                <h3 className="font-serif font-bold text-2xl text-forest mb-6">Apply Now</h3>
                
                {submitted ? (
                  <div className="bg-forest/5 p-8 text-center rounded-sm border border-forest/10 mt-4">
                    <CheckCircle2 className="w-12 h-12 text-gold mx-auto mb-4" />
                    <h4 className="text-gold font-serif font-bold text-xl mb-3">Application Received.</h4>
                    <p className="text-forest/70 font-normal text-sm">
                      Thank you for your interest. Our talent acquisition team will review your CV and be in touch.
                    </p>
                  </div>
                ) : (
                  <form onSubmit={handleSubmit} className="space-y-6">
                    <div className="space-y-2">
                      <label htmlFor="name" className="text-xs font-bold uppercase tracking-widest text-forest/70 block">
                        Full Name
                      </label>
                      <input 
                        type="text" 
                        id="name"
                        required 
                        className="w-full bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-forest font-normal"
                        placeholder="e.g. John Doe"
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <label htmlFor="email" className="text-xs font-bold uppercase tracking-widest text-forest/70 block">
                        Email Address
                      </label>
                      <input 
                        type="email" 
                        id="email" 
                        required
                        className="w-full bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-forest font-normal"
                        placeholder="john@example.com"
                      />
                    </div>

                    <div className="space-y-2">
                      <label htmlFor="position" className="text-xs font-bold uppercase tracking-widest text-forest/70 block">
                        Position
                      </label>
                      <select 
                        id="position" 
                        required
                        className="w-full bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-forest font-normal appearance-none"
                      >
                        <option value="icc_lawyer">ICC Rules Lawyer</option>
                        <option value="general">General Application</option>
                      </select>
                    </div>

                    <div className="space-y-2">
                      <label htmlFor="cv" className="text-xs font-bold uppercase tracking-widest text-forest/70 block flex items-center gap-2">
                        Upload CV <span className="text-[10px] lowercase font-normal">(PDF only, Max: 5MB)</span>
                      </label>
                      <div className="relative group">
                        <input 
                          type="file" 
                          id="cv" 
                          accept=".pdf"
                          required
                          onChange={handleFileChange}
                          className="w-full text-forest/70 bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-sm file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-gold/10 file:text-gold hover:file:bg-gold/20"
                        />
                      </div>
                      {fileError && <p className="text-red-500 text-xs font-medium mt-1">{fileError}</p>}
                    </div>

                    <div className="pt-2">
                      <Turnstile
                        siteKey="0x4AAAAAACul__dWFbvMuQKG"
                        onSuccess={(token) => setToken(token)}
                        options={{ size: "normal", theme: "light" }}
                      />
                    </div>

                    <button 
                      type="submit" 
                      disabled={isSubmitting || !token || !!fileError}
                      className="w-full bg-forest hover:bg-forest/90 disabled:bg-forest/50 text-offwhite font-medium uppercase tracking-widest text-sm py-4 rounded-sm transition-colors mt-6 flex justify-center items-center"
                    >
                      {isSubmitting ? "Submitting..." : "Submit Application"}
                    </button>
                  </form>
                )}
              </AnimatedSection>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
