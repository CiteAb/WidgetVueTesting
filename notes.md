# API Structure Reference

# Endpoints

### Citations

#### Request params

PubMed only (true/false)
Preprints only (true/false)
Only with images (true/false)

Reactants
Applications
Research areas
Reagent type
Country
Journal
Institution
Validation
Instrument used
Dilution

```json
  {
    "filters": {
      "reactants": [1, 5, 6],
      "applications": [2, 3],
      "reagentTypes": ["Antibody", "SmallMolecule"]
    },
    "cursor": "xxx"
  }
```


#### Example Response
```json
  {
    "results": [{
        "title": "test",
        "journal": "plos one",
        "authors": ["Rob", "Joe"],
        "abstract": "Something about stuff",
        "reactants": ["Human"],
        "applications": ["Wb"],
        "figureIds": [123, 456, 789]
    }],
    "totalCitations": 150,
    "nextCursor": "yyy"
  }
```

### Images

#### Request params

Filters are the same as citations

```json
  {
    "filters": {
      "reactants": [1, 5, 6],
      "applications": [2, 3],
      "reagentTypes": ["Antibody", "SmallMolecule"]
    },
    "cursor": "xxx"
  }
```

#### Example Response
```json
  {
    "results": [{
        "id": 123,
        "urls": {
            "full": "www.images.com/full",
            "medium": "www.images.com/medium",
            "small": "www.images.com/small"
        },
        "caption": "Some caption",
        "relatedProducts": [
          {
            "code": "xxx",
            "name": "Reagent 1",
            "company": "Millipore"
          }
        ]
    }],
    "totalImages": 150,
    "nextCursor": "yyy"
  }
```

### Aggregate Metrics

#### Request params

Filters are the same as citations

```json
  {
    "filters": {
      "productCodes": ["cd123"],
      "reactants": [1, 5, 6],
      "applications": [2, 3],
      "reagentTypes": ["Antibody", "SmallMolecule"]
    },
    "aggregateKey": "country"
  }
```

#### Example Response
```json
  {
    "results": {
        "UK": 123,
        "France": 456
    }
  }
```

### Setup

```json
  {
    "filters": {
      "productCodes": ["ab1", "ab2"]
    }
  }
```

#### Example Response
```json
  {
    "facets": {
      "reactants": [{"name": "x", "id": 7}],
    },
    "enabledFeatures": ["map", "imageCarousel", "citations"],
    "stylesheet": "url_here"
  }
```