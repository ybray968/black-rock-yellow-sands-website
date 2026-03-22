"use client";

import { COMPANY } from "@/lib/siteData";

export default function PrivacyPolicyPage() {
  return (
    <div className="bg-offwhite min-h-screen pt-32 pb-24">
      <div className="container mx-auto px-4 md:px-8 max-w-4xl text-forest">
        <h1 className="text-4xl md:text-5xl font-serif font-bold uppercase tracking-tighter mb-8 bg-forest text-offwhite py-6 px-8 rounded-sm">
          Privacy <span className="text-gold italic font-normal">Policy.</span>
        </h1>

        <div className="space-y-8 font-normal leading-relaxed text-forest/80 text-lg text-balance">
          <p>
            <strong>Last Updated:</strong> {new Date().toLocaleDateString()}
          </p>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              1. Information We Collect
            </h2>
            <p className="mb-4">
              {COMPANY.name} operates strictly on a B2B model. We only collect
              professional and corporate data necessary to fulfill wholesale inquiries,
              logistics coordination, and legal compliance.
            </p>
            <ul className="list-disc pl-6 space-y-2 marker:text-gold">
              <li>Corporate email addresses and contact names via our inquiry forms.</li>
              <li>Company registration numbers (CR) and tax identifiers (VATIN).</li>
              <li>IP addresses and browser telemetry collected securely against bots (Cloudflare Turnstile).</li>
            </ul>
          </section>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              2. How We Use Your Data
            </h2>
            <p className="mb-4">
              The data collected is utilized entirely for the purpose of facilitating
              international trade, responding to supply quotas, and verifying
              business credibility. We do not sell, license, or broker your corporate
              information to third parties.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              3. Data Security
            </h2>
            <p className="mb-4">
              The integrity of our supply chains is mirrored in our data policy. We
              deploy enterprise-grade encryption and secure networking protocols
              across all our digital infrastructure to prevent unauthorized access
              or disclosure of your material orders and corporate details.
            </p>
          </section>

          <section>
            <h2 className="text-2xl font-serif font-bold text-forest mb-4">
              4. Contact the Data Controller
            </h2>
            <p className="mb-4">
              For any privacy inquiries or to request deletion of your corporate
              data from our active records, please direct correspondence to the
              administrative office:
              <br />
              <br />
              <strong>Email:</strong> {COMPANY.email}
              <br />
              <strong>Address:</strong> {COMPANY.address}
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
