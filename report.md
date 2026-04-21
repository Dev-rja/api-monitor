# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 16:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.11% | 3618.5 | 10206.7 | 1000ms | 141/416 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.4 | 4088.9 | 1500ms | 2/416 |
| ❌ | `nasa_apod` | 61.78% | 37.74% | 4337.4 | 10549.1 | 2000ms | 259/416 |
| ❌ | `ipapi_check` | 93.75% | 100.0% | 159.0 | 353.0 | 2500ms | 0/416 |
| ⚠️ | `open_meteo_weather` | 98.08% | 96.88% | 747.0 | 14877.1 | 2000ms | 13/416 |
| ⚠️ | `dog_ceo_random` | 99.28% | 89.9% | 876.1 | 10244.1 | 2500ms | 42/416 |
| ✅ | `catfact_random` | 99.28% | 99.28% | 276.7 | 10080.2 | 3000ms | 3/416 |
| ✅ | `useless_fact` | 99.52% | 99.04% | 586.1 | 10229.6 | 2500ms | 4/416 |
| ✅ | `agify_name` | 100.0% | 99.76% | 373.0 | 3237.1 | 2000ms | 1/416 |
| ✅ | `rest_countries` | 100.0% | 99.04% | 259.4 | 7269.1 | 2500ms | 4/416 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.8 | 2314.9 | 2000ms | 1/416 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/416 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5778.8 | 70.83% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5164.2 | 64.0% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `numbers_trivia` | 12:00 | 4658.8 | 44.44% |
| `nasa_apod` | 12:00 | 4598.1 | 66.67% |
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
