# -*- coding: utf-8 -*-
from setting import db

# 定义browse_deg_table表的模型
class test(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    ana_group = db.Column(db.String(50))
    # ... 其他列省略
    def to_json(self):
        # 将查询结果转化为字典格式
        return {
            'id': self.id,
            'ana_group': self.ana_group,
            # ... 其他列省略
        }

class KeggGene(db.Model):
    __tablename__ = 'kegg_infomation_for_every_gene'

    id = db.Column(db.Integer, primary_key=True)
    GeneID = db.Column(db.String(50))
    pathwayID = db.Column(db.String(50))
    Pathway = db.Column(db.String(255))
    Gene_Symbol = db.Column(db.String(50))
    Organism = db.Column(db.String(50))
    # ... 其他列省略
    def to_json_kegg(self):
        return {
            'id': self.id,
            'GeneID': self.GeneID,
            'pathwayID': self.pathwayID,
            'Pathway': self.Pathway,
            'Gene_Symbol': self.Gene_Symbol,
            'Organism': self.Organism,
        }

class GeneInfo(db.Model):
    __tablename__ = 'gene_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Gene_Symbol = db.Column(db.String(255), nullable=True)
    Organism = db.Column(db.String(255), nullable=True)
    Description = db.Column(db.String(255), nullable=True)
    Gene_ID = db.Column(db.String(255), nullable=True)
    Ensembl_ID = db.Column(db.String(255), nullable=True)
    Chromosome = db.Column(db.String(255), nullable=True)
    Strand = db.Column(db.String(255), nullable=True)
    Gene_Type = db.Column(db.String(255), nullable=True)
    Synonyms = db.Column(db.String(255), nullable=True)
    Start = db.Column(db.String(255), nullable=True)
    End = db.Column(db.String(255), nullable=True)
    Location = db.Column(db.String(255), nullable=True)
    methy_p = db.Column(db.String(255), nullable=True)
    methy_fdr = db.Column(db.String(255), nullable=True)
    methy_log2FC = db.Column(db.String(255), nullable=True)
    methy_Tissue = db.Column(db.String(255), nullable=True)
    methy_Platform = db.Column(db.String(255), nullable=True)
    methy_dataset = db.Column(db.String(255), nullable=True)
    methy_Pain_Type = db.Column(db.String(255), nullable=True)
    methy_position = db.Column(db.String(255), nullable=True)
    variant_rs_number = db.Column(db.String(255), nullable=True)
    variant_position = db.Column(db.String(255), nullable=True)
    variant_alternate_allele = db.Column(db.String(255), nullable=True)
    GMAF = db.Column(db.String(255), nullable=True)
    Alleles = db.Column(db.String(255), nullable=True)
    phenotype_description = db.Column(db.String(255), nullable=True)
    phenotype_direction = db.Column(db.String(255), nullable=True)
    result_comments = db.Column(db.String(255), nullable=True)
    publication_pmid = db.Column(db.String(255), nullable=True)
    Database = db.Column(db.String(255), nullable=True)

    def to_json_geneinfo(self):
        return {
            'id': self.id,
            'Gene_Symbol': self.Gene_Symbol,
            'Organism': self.Organism,
            'Description': self.Description,
            'Gene_ID': self.Gene_ID,
            'Ensembl_ID': self.Ensembl_ID,
            'Chromosome': self.Chromosome,
            'Strand': self.Strand,
            'Gene_Type': self.Gene_Type,
            'Synonyms': self.Synonyms,
            'Start': self.Start,
            'End': self.End,
            'Location': self.Location,
            'methy_p': self.methy_p,
            'methy_fdr': self.methy_fdr,
            'methy_log2FC': self.methy_log2FC,
            'methy_Tissue': self.methy_Tissue,
            'methy_Platform': self.methy_Platform,
            'methy_dataset': self.methy_dataset,
            'methy_Pain_Type': self.methy_Pain_Type,
            'methy_position': self.methy_position,
            'variant_rs_number': self.variant_rs_number,
            'variant_position': self.variant_position,
            'variant_alternate_allele': self.variant_alternate_allele,
            'GMAF': self.GMAF,
            'Alleles': self.Alleles,
            'phenotype_description': self.phenotype_description,
            'phenotype_direction': self.phenotype_direction,
            'result_comments': self.result_comments,
            'publication_pmid': self.publication_pmid,
            'Database': self.Database,
        }

class AnalysisInfo(db.Model):
    __tablename__ = 'analysis_information'

    id = db.Column(db.Integer, primary_key=True)
    Analysis_id = db.Column(db.String(255), default=None)
    dataset = db.Column(db.String(255), default=None)
    GEOaccession = db.Column(db.String(255), default=None)
    Pain_type = db.Column(db.String(255), default=None)
    Tissue = db.Column(db.String(255), default=None)
    Organism = db.Column(db.String(255), default=None)
    Treated = db.Column(db.String(255), default=None)
    Control = db.Column(db.String(255), default=None)
    Design = db.Column(db.String(255), default=None)
    T_sample = db.Column(db.String(255), default=None)
    C_sample = db.Column(db.String(255), default=None)
    Filename = db.Column(db.String(255), default=None)
    description = db.Column(db.String(1000), default=None)
    PMID = db.Column(db.String(255), default=None)
    title = db.Column(db.String(255), default=None)
    ana_group = db.Column(db.String(255), default=None)
    DEG_num = db.Column(db.String(255), default=None)
    Detail = db.Column(db.String(255), default=None)
    related_Ana = db.Column(db.String(255), default=None)

    def to_json_analysis_info(self):
        return {
            'id': self.id,
            'Analysis_id': self.Analysis_id,
            'dataset': self.dataset,
            'GEOaccession': self.GEOaccession,
            'Pain_type': self.Pain_type,
            'Tissue': self.Tissue,
            'Organism': self.Organism,
            'Treated': self.Treated,
            'Control': self.Control,
            'Design': self.Design,
            'T_sample':  self.T_sample.split(',') if self.T_sample else [],
            'C_sample': self.C_sample.split(',') if self.C_sample else [],
            'Filename': self.Filename,
            'description': self.description,
            'PMID': self.PMID,
            'title': self.title,
            'ana_group': self.ana_group,
            'DEG_num': self.DEG_num,
            'Detail': self.Detail,
            'related_Ana': self.related_Ana.split(',')
        }

class SampleInfo(db.Model):
    __tablename__ = 'tpeadetail_sampleinfo'

    id = db.Column(db.Integer, primary_key=True)
    dataset = db.Column(db.String(255))
    GEOaccession = db.Column(db.String(255))
    Organism = db.Column(db.String(255))
    Pain_type = db.Column(db.String(255))
    GSM = db.Column(db.String(255))
    Tissue = db.Column(db.String(255))
    Sample_info = db.Column(db.String(255))
    Sample_info2 = db.Column(db.String(255))
    Condition = db.Column(db.String(255))
    datatype = db.Column(db.String(255))
    Detail = db.Column(db.String(255))
    Analysis_id = db.Column(db.String(255))

    def to_json_sample_info(self):
        return {
            'id': self.id,
            'dataset': self.dataset,
            'GEOaccession': self.GEOaccession,
            'Organism': self.Organism,
            'Pain_type': self.Pain_type,
            'GSM': self.GSM,
            'Tissue': self.Tissue,
            'Sample_info': self.Sample_info,
            'Sample_info2': self.Sample_info2,
            'Condition': self.Condition,
            'datatype': self.datatype,
            'Detail': self.Detail,
            'Analysis_id': self.Analysis_id
        }

class KeggResult(db.Model):
    __tablename__ = 'tpeadetail_keggresults'

    id = db.Column(db.Integer, primary_key=True)
    KeggID = db.Column(db.String(255))
    Description = db.Column(db.String(255))
    GeneRatio = db.Column(db.String(255))
    BgRatio = db.Column(db.String(255))
    pvalue = db.Column(db.String(255))
    p_adjust = db.Column(db.String(255))
    qvalue = db.Column(db.String(255))
    geneID = db.Column(db.String(255))
    Count = db.Column(db.String(255))
    geneName = db.Column(db.String(255))
    gene_type = db.Column(db.String(255))
    Analysis_id = db.Column(db.String(255))
    log10pv = db.Column(db.String(255))

    def to_json_kegg_result(self):
        return {
            'id': self.id,
            'KeggID': self.KeggID,
            'Description': self.Description,
            'GeneRatio': self.GeneRatio,
            'BgRatio': self.BgRatio,
            'pvalue': self.pvalue,
            'p_adjust': self.p_adjust,
            'qvalue': self.qvalue,
            'geneID': self.geneID,
            'Count': self.Count,
            'geneName': self.geneName,
            'gene_type': self.gene_type,
            'Analysis_id': self.Analysis_id,
            'log10pv': self.log10pv
        }

class BrowseTable(db.Model):
    __tablename__ = 'browse_deg_table'

    id = db.Column(db.Integer, primary_key=True)
    Organism = db.Column(db.String(255), nullable=True)
    Tissue = db.Column(db.String(255), nullable=True)
    # ana_group = db.Column(db.String(255), nullable=True)
    Analysis_id = db.Column(db.String(255), nullable=True)
    dataset = db.Column(db.String(255), nullable=True)
    Pain_type = db.Column(db.String(255), nullable=True)
    Detail = db.Column(db.String(255), nullable=True)
    Gene_Symbol = db.Column(db.String(255), nullable=True)
    log2fc = db.Column(db.String(255), nullable=True)
    pvalue = db.Column(db.String(255), nullable=True)
    padj = db.Column(db.String(255), nullable=True)
    # con_value = db.Column(db.String(255), nullable=True)
    # exp_value = db.Column(db.String(255), nullable=True)
    # design = db.Column(db.String(255), nullable=True)
    # Ensembl_ID = db.Column(db.String(255), nullable=True)
    # Gene_ID = db.Column(db.String(255), nullable=True)
    # up_score = db.Column(db.String(255), nullable=True)
    # down_score = db.Column(db.String(255), nullable=True)
    rra_score = db.Column(db.String(255), nullable=True)
    # GEOaccession = db.Column(db.String(255), nullable=True)
    # DEG_num = db.Column(db.String(255), nullable=True)

    def to_json_browse(self):
        try:
            log2fc_rounded = round(float(self.log2fc), 4)
        except ValueError:
            log2fc_rounded = self.log2fc

        return {
            'id': self.id,
            'Organism': self.Organism,
            'Tissue': self.Tissue,
            # 'ana_group': self.ana_group,
            'Analysis_id': self.Analysis_id,
            'dataset': self.dataset,
            'Pain_type': self.Pain_type,
            'Detail': self.Detail,
            'Gene_Symbol': self.Gene_Symbol,
            'log2fc': log2fc_rounded,
            'pvalue': self.pvalue,
            'padj': self.padj,
            # 'con_value': self.con_value,
            # 'exp_value': self.exp_value,
            # 'design': self.design,
            # 'Ensembl_ID': self.Ensembl_ID,
            # 'Gene_ID': self.Gene_ID,
            # 'up_score': self.up_score,
            # 'down_score': self.down_score,
            'rra_score': self.rra_score,
            # 'GEOaccession': self.GEOaccession,
            # 'DEG_num': self.DEG_num,
        }


class DiffexprTable(db.Model):
    __tablename__ = 'diff_table'

    id = db.Column(db.Integer, primary_key=True)
    Gene_Symbol = db.Column(db.String(255))
    Organism = db.Column(db.String(255))
    Tissue = db.Column(db.String(255))
    ana_group = db.Column(db.String(255))
    Analysis_id = db.Column(db.String(255))
    dataset = db.Column(db.String(255))
    Pain_type = db.Column(db.String(255))
    Detail = db.Column(db.String(255))
    log2fc = db.Column(db.String(5))
    pvalue = db.Column(db.String(255))
    padj = db.Column(db.String(255))
    con_value = db.Column(db.String(255))
    exp_value = db.Column(db.String(255))
    design = db.Column(db.String(255))
    Ensembl_ID = db.Column(db.String(255))
    Gene_ID = db.Column(db.String(255))
    up_score = db.Column(db.String(255))
    down_score = db.Column(db.String(255))
    rra_score = db.Column(db.String(255))
    GEOaccession = db.Column(db.String(255))
    DEG_num = db.Column(db.String(255))
    id1 = db.Column(db.String(255))
    Description = db.Column(db.String(255))
    Chromosome = db.Column(db.String(255))
    Strand = db.Column(db.String(255))
    Gene_Type = db.Column(db.String(255))
    Synonyms = db.Column(db.String(255))
    Start = db.Column(db.String(255))
    End = db.Column(db.String(255))
    Location = db.Column(db.String(255))
    methy_p = db.Column(db.String(255))
    methy_fdr = db.Column(db.String(255))
    methy_log2FC = db.Column(db.String(255))
    methy_Tissue = db.Column(db.String(255))
    methy_Platform = db.Column(db.String(255))
    methy_dataset = db.Column(db.String(255))
    methy_Pain_Type = db.Column(db.String(255))
    methy_position = db.Column(db.String(255))
    variant_rs_number = db.Column(db.String(255))
    variant_position = db.Column(db.String(255))
    variant_alternate_allele = db.Column(db.String(255))
    GMAF = db.Column(db.String(255))
    Alleles = db.Column(db.String(255))
    phenotype_description = db.Column(db.String(255))
    phenotype_direction = db.Column(db.String(255))
    result_comments = db.Column(db.String(255))
    publication_pmid = db.Column(db.String(255))
    Database = db.Column(db.String(255))

    def diffexpr_to_json(self):
        try:
            log2fc_rounded = round(float(self.log2fc), 4)
        except ValueError:
            log2fc_rounded = self.log2fc

        return {
            'id': self.id,
            'Gene_Symbol': self.Gene_Symbol,
            'Organism': self.Organism,
            'Tissue': self.Tissue,
            'ana_group': self.ana_group,
            'Analysis_id': self.Analysis_id,
            'dataset': self.dataset,
            'Pain_type': self.Pain_type,
            'Detail': self.Detail,
            'log2fc': log2fc_rounded,
            'pvalue': self.pvalue,
            'padj': self.padj,
            'con_value': self.con_value,
            'exp_value': self.exp_value,
            'design': self.design,
            'Ensembl_ID': self.Ensembl_ID,
            'Gene_ID': self.Gene_ID,
            'up_score': self.up_score,
            'down_score': self.down_score,
            'rra_score': self.rra_score,
            'GEOaccession': self.GEOaccession,
            'DEG_num': self.DEG_num,
            'id1': self.id1,
            'Description': self.Description,
            'Chromosome': self.Chromosome,
            'Strand': self.Strand,
            'Gene_Type': self.Gene_Type,
            'Synonyms': self.Synonyms,
            'Start': self.Start,
            'End': self.End,
            'Location': self.Location,
            'methy_p': self.methy_p,
            'methy_fdr': self.methy_fdr,
            'methy_log2FC': self.methy_log2FC,
            'methy_Tissue': self.methy_Tissue,
            'methy_Platform': self.methy_Platform,
            'methy_dataset': self.methy_dataset,
            'methy_Pain_Type': self.methy_Pain_Type,
            'methy_position': self.methy_position,
            'variant_rs_number': self.variant_rs_number,
            'variant_position': self.variant_position,
            'variant_alternate_allele': self.variant_alternate_allele,
            'GMAF': self.GMAF,
            'Alleles': self.Alleles,
            'phenotype_description': self.phenotype_description,
            'phenotype_direction': self.phenotype_direction,
            'result_comments': self.result_comments,
            'publication_pmid': self.publication_pmid,
            'Database': self.Database
        }


