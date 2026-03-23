"use client";

import { useState } from "react";
import Image from "next/image";
import {
  AnimatedSection,
  StaggerContainer,
  StaggerItem,
} from "@/components/AnimatedSection";
import { Mail, MapPin, Phone, MessageSquare } from "lucide-react";
import { COMPANY } from "@/lib/siteData";
import { Turnstile } from "@marsidev/react-turnstile";

export default function ContactPage() {
  const [token, setToken] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!token) {
      alert("Please complete the bot protection check.");
      return;
    }
    
    setIsSubmitting(true);
    
    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: (document.getElementById("name") as HTMLInputElement).value,
          email: (document.getElementById("email") as HTMLInputElement).value,
          division: (document.getElementById("division") as HTMLSelectElement).value,
          message: (document.getElementById("message") as HTMLTextAreaElement).value,
        }),
      });

      if (response.ok) {
        setSubmitted(true);
      } else {
        alert("Failed to send message. Please try again later.");
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
        <div className="absolute inset-0 z-0">
          <Image
            src="/images/contact_us_hero.png"
            alt="Bulker ship representing global reach"
            fill
            priority
            className="object-cover object-center opacity-40 hover:opacity-60 transition-opacity duration-1000"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-forest via-forest/80 to-transparent" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <StaggerContainer className="max-w-3xl">
            <StaggerItem direction="up" className="mb-6">
              <h1 className="text-5xl md:text-7xl font-serif font-bold text-offwhite uppercase tracking-tighter leading-[0.9]">
                Contact <br /> Us
              </h1>
            </StaggerItem>
            <StaggerItem direction="up">
              <p className="text-offwhite/80 text-lg md:text-xl font-normal leading-relaxed max-w-xl text-balance">
                Request a wholesale quote, establish logistical partnerships, or reach
                out for structural engineering material inquiries.
              </p>
            </StaggerItem>
          </StaggerContainer>
        </div>
      </section>

      {/* 2. CONTACT DETAILS & FORM */}
      <section className="py-24 md:py-32 relative z-10 bg-offwhite">
        <div className="container mx-auto px-4 md:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24">
            
            {/* Contact Details */}
            <div>
              <AnimatedSection direction="up" className="mb-12">
                <h2 className="text-3xl md:text-4xl font-serif font-bold text-forest mb-4">
                  Corporate Office
                </h2>
                <div className="w-16 h-px bg-gold mb-8" />
                <p className="text-forest/70 font-normal text-lg mb-12 text-balance leading-relaxed">
                  Our team is ready to process your wholesale supply quotas. Reach
                  out to us via our dedicated lines or through the inquiry form.
                </p>
              </AnimatedSection>

              <StaggerContainer className="space-y-8">
                {/* Email */}
                <StaggerItem direction="left" className="flex items-start gap-6 group">
                  <div className="p-4 bg-forest/5 rounded-full group-hover:bg-gold/10 transition-colors">
                    <Mail className="w-6 h-6 text-forest group-hover:text-gold transition-colors" />
                  </div>
                  <div>
                    <h3 className="font-serif font-bold text-xl text-forest mb-1">Email Inquiry</h3>
                    <a href={`mailto:${COMPANY.email}`} className="text-forest/70 font-normal hover:text-gold transition-colors">
                      {COMPANY.email}
                    </a>
                  </div>
                </StaggerItem>

                {/* Phone */}
                <StaggerItem direction="left" className="flex items-start gap-6 group">
                  <div className="p-4 bg-forest/5 rounded-full group-hover:bg-gold/10 transition-colors">
                    <Phone className="w-6 h-6 text-forest group-hover:text-gold transition-colors" />
                  </div>
                  <div>
                    <h3 className="font-serif font-bold text-xl text-forest mb-1">Direct Line</h3>
                    <a href={`tel:${COMPANY.phone}`} className="text-forest/70 font-normal hover:text-gold transition-colors">
                      {COMPANY.phone}
                    </a>
                  </div>
                </StaggerItem>

                {/* Location */}
                <StaggerItem direction="left" className="flex items-start gap-6 group">
                  <div className="p-4 bg-forest/5 rounded-full group-hover:bg-gold/10 transition-colors">
                    <MapPin className="w-6 h-6 text-forest group-hover:text-gold transition-colors" />
                  </div>
                  <div>
                    <h3 className="font-serif font-bold text-xl text-forest mb-1">Headquarters</h3>
                    <address className="text-forest/70 font-normal not-italic leading-relaxed max-w-[200px]">
                      {COMPANY.address}
                    </address>
                  </div>
                </StaggerItem>
              </StaggerContainer>
            </div>

            {/* Contact Form */}
            <AnimatedSection direction="up" delay={0.2} className="bg-white p-8 md:p-12 border border-forest/10 rounded-sm shadow-xl shadow-forest/5 h-fit">
              <h3 className="font-serif font-bold text-2xl text-forest mb-6">Inquiry Form</h3>
              
              {submitted ? (
                <div className="bg-forest/5 p-8 text-center rounded-sm border border-forest/10">
                  <h4 className="text-gold font-serif font-bold text-xl mb-3">Inquiry Received.</h4>
                  <p className="text-forest/70 font-normal text-sm">
                    A corporate representative will carefully review your request and get back to you shortly.
                  </p>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="space-y-2">
                      <label htmlFor="name" className="text-xs font-bold uppercase tracking-widest text-forest/70 block">
                        Full Name / Company
                      </label>
                      <input 
                        type="text" 
                        id="name"
                        required 
                        className="w-full bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-forest font-normal"
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
                      />
                    </div>
                  </div>

                  <div className="space-y-2">
                    <label htmlFor="division" className="text-xs font-bold uppercase tracking-widest text-forest/70 block">
                      Division of Interest
                    </label>
                    <select 
                      id="division" 
                      required
                      className="w-full bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-forest font-normal appearance-none"
                    >
                      <option value="">Select Division...</option>
                      <option value="agriculture">Agriculture</option>
                      <option value="construction">Industrial Construction</option>
                      <option value="sulfur">Sulfur Trading</option>
                      <option value="other">Other / General</option>
                    </select>
                  </div>

                  <div className="space-y-2">
                    <label htmlFor="message" className="text-xs font-bold uppercase tracking-widest text-forest/70 block">
                      Message / Request Details
                    </label>
                    <textarea 
                      id="message" 
                      rows={5}
                      required
                      className="w-full bg-forest/5 border border-forest/10 px-4 py-3 rounded-sm focus:outline-none focus:border-gold transition-colors text-forest font-normal resize-none"
                    ></textarea>
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
                    disabled={isSubmitting || !token}
                    className="w-full bg-forest hover:bg-forest/90 disabled:bg-forest/50 text-offwhite font-medium uppercase tracking-widest text-sm py-4 rounded-sm transition-colors mt-6 flex justify-center items-center"
                  >
                    {isSubmitting ? "Submitting..." : "Send Request"}
                  </button>
                </form>
              )}
            </AnimatedSection>
            
          </div>
        </div>
      </section>
    </div>
  );
}
