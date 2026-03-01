#!/usr/bin/env python3
"""
Extract text from all PDFs in the Ley 1178 course directory
and output them as Markdown files.
"""
import pdfplumber
import os
import sys
import re

SOURCE_DIR = r"C:\Users\dell_\Desktop\Trabajo\Cursos\1178"
OUTPUT_DIR = r"C:\Users\dell_\Desktop\Trabajo\Cursos\1178\knowledge-base"

# Mapping of PDF files to their output structure
PDF_MAPPINGS = {
    # Ley completa
    "Ley_Nro_1178.pdf": ("ley-1178", "ley_1178_texto.md", "Ley N° 1178 - Ley de Administración y Control Gubernamentales"),
    
    # Temas principales
    "TEMA_1.pdf": ("temas", "tema_01.md", "Tema 1"),
    "TEMA_2.pdf": ("temas", "tema_02.md", "Tema 2"),
    "TEMA_3.pdf": ("temas", "tema_03.md", "Tema 3"),
    "TEMA_4.pdf": ("temas", "tema_04.md", "Tema 4"),
    "TEMA_5.pdf": ("temas", "tema_05.md", "Tema 5"),
    "TEMA_6.pdf": ("temas", "tema_06.md", "Tema 6"),
    "TEMA_7.pdf": ("temas", "tema_07.md", "Tema 7"),
    "TEMA_8.pdf": ("temas", "tema_08.md", "Tema 8"),
    "TEMA_9.pdf": ("temas", "tema_09.md", "Tema 9"),
    "TEMA_10.pdf": ("temas", "tema_10.md", "Tema 10"),
    
    # Subtemas Unidad 2
    "1. U2_T2_ ST1_INTRODUCCION_DLaura.pdf": ("subtemas", "st01_introduccion.md", "Subtema 1 - Introducción"),
    "2. U2_T2_ST2_SPIE_DLaura.pdf": ("subtemas", "st02_spie.md", "Subtema 2 - Sistema de Planificación Integral del Estado (SPIE)"),
    "3. U2_T2_ST3_SPO_DLaura.pdf": ("subtemas", "st03_spo.md", "Subtema 3 - Sistema de Programación de Operaciones (SPO)"),
    "4. U2_T2_ST4_SP_DLaura.pdf": ("subtemas", "st04_sp.md", "Subtema 4 - Sistema de Presupuesto (SP)"),
    "5._20U2_T2_ST5_SOA_DLaura.pdf": ("subtemas", "st05_soa.md", "Subtema 5 - Sistema de Organización Administrativa (SOA)"),
    "6. U2_T2_ST6_SAP_DLaura.pdf": ("subtemas", "st06_sap.md", "Subtema 6 - Sistema de Administración de Personal (SAP)"),
    "7. U2_T2_ST7_SABS_DLaura.pdf": ("subtemas", "st07_sabs.md", "Subtema 7 - Sistema de Administración de Bienes y Servicios (SABS)"),
    "8. U2_T2_ST8_STyCP_DLaura.pdf": ("subtemas", "st08_stycp.md", "Subtema 8 - Sistema de Tesorería y Crédito Público (STyCP)"),
    "9. U2_T2_ST9_SCI_DLaura.pdf": ("subtemas", "st09_sci.md", "Subtema 9 - Sistema de Contabilidad Integrada (SCI)"),
    "10. U2_T2_ST10_SCG_DLaura.pdf": ("subtemas", "st10_scg.md", "Subtema 10 - Sistema de Control Gubernamental (SCG)"),
}

# Complementos
COMPLEMENTOS_MAPPINGS = {
    "1.1._20PGDES_20Ley_N_650_20(2).pdf": ("complementos", "pgdes_ley_650.md", "Plan General de Desarrollo Económico y Social - Ley N° 650"),
    "1.2. AGENDA 2025.pdf": ("complementos", "agenda_2025.md", "Agenda Patriótica 2025"),
    "2.1. NB-SPO.pdf": ("complementos", "nb_spo.md", "Normas Básicas del Sistema de Programación de Operaciones (NB-SPO)"),
    "2.2._20NB-SP.pdf": ("complementos", "nb_sp.md", "Normas Básicas del Sistema de Presupuesto (NB-SP)"),
    "2.4. NB-SAP.pdf": ("complementos", "nb_sap.md", "Normas Básicas del Sistema de Administración de Personal (NB-SAP)"),
    "2.5. NB-SABS.pdf": ("complementos", "nb_sabs.md", "Normas Básicas del Sistema de Administración de Bienes y Servicios (NB-SABS)"),
    "2.8. NB-SCI.pdf": ("complementos", "nb_sci.md", "Normas Básicas del Sistema de Contabilidad Integrada (NB-SCI)"),
    "Unidad 2 Ley 2341 Procedimiento Administrativo.pdf": ("complementos", "ley_2341_procedimiento_administrativo.md", "Ley N° 2341 - Procedimiento Administrativo"),
    "curso LMAD Texto diagramado - sin slogan.pdf": ("complementos", "lmad.md", "Ley Marco de Autonomías y Descentralización (LMAD)"),
}


def clean_text(text):
    """Clean extracted text for better markdown formatting."""
    if not text:
        return ""
    # Remove excessive whitespace but keep paragraph breaks
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove trailing whitespace from lines
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    return text


def extract_pdf_to_markdown(pdf_path, title):
    """Extract text from a PDF and format as Markdown."""
    content_parts = []
    content_parts.append(f"# {title}\n")
    content_parts.append(f"> **Fuente:** `{os.path.basename(pdf_path)}`\n")
    content_parts.append("---\n")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            content_parts.append(f"*Documento de {total_pages} páginas*\n")
            
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    cleaned = clean_text(text)
                    if cleaned.strip():
                        content_parts.append(f"\n## Página {i + 1}\n")
                        content_parts.append(cleaned)
                        content_parts.append("")
    except Exception as e:
        content_parts.append(f"\n> ⚠️ Error al extraer: {str(e)}\n")
    
    return '\n'.join(content_parts)


def main():
    # Create output directories
    for subdir in ["ley-1178", "temas", "subtemas", "complementos", "recursos"]:
        os.makedirs(os.path.join(OUTPUT_DIR, subdir), exist_ok=True)
    
    total = 0
    errors = 0
    
    # Process main directory PDFs
    for pdf_name, (subdir, md_name, title) in PDF_MAPPINGS.items():
        pdf_path = os.path.join(SOURCE_DIR, pdf_name)
        if not os.path.exists(pdf_path):
            print(f"[WARN] No encontrado: {pdf_name}")
            errors += 1
            continue
        
        print(f"[OK] Procesando: {pdf_name} -> {subdir}/{md_name}")
        md_content = extract_pdf_to_markdown(pdf_path, title)
        
        output_path = os.path.join(OUTPUT_DIR, subdir, md_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        total += 1
    
    # Process complementos
    for pdf_name, (subdir, md_name, title) in COMPLEMENTOS_MAPPINGS.items():
        pdf_path = os.path.join(SOURCE_DIR, "Complementos", pdf_name)
        if not os.path.exists(pdf_path):
            print(f"[WARN] No encontrado: Complementos/{pdf_name}")
            errors += 1
            continue
        
        print(f"[OK] Procesando: Complementos/{pdf_name} -> {subdir}/{md_name}")
        md_content = extract_pdf_to_markdown(pdf_path, title)
        
        output_path = os.path.join(OUTPUT_DIR, subdir, md_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        total += 1
    
    print(f"\n{'='*50}")
    print(f"Procesados: {total} archivos")
    print(f"Errores: {errors}")
    print(f"Directorio de salida: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
