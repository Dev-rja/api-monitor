# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 17:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.95% | 3633.8 | 10206.7 | 1000ms | 142/417 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.2 | 4088.9 | 1500ms | 2/417 |
| ❌ | `nasa_apod` | 61.63% | 37.65% | 4351.6 | 10549.1 | 2000ms | 260/417 |
| ❌ | `ipapi_check` | 93.53% | 100.0% | 159.0 | 353.0 | 2500ms | 0/417 |
| ⚠️ | `open_meteo_weather` | 98.08% | 96.88% | 746.6 | 14877.1 | 2000ms | 13/417 |
| ⚠️ | `dog_ceo_random` | 99.28% | 89.93% | 875.5 | 10244.1 | 2500ms | 42/417 |
| ✅ | `catfact_random` | 99.28% | 99.28% | 276.3 | 10080.2 | 3000ms | 3/417 |
| ✅ | `useless_fact` | 99.52% | 99.04% | 585.9 | 10229.6 | 2500ms | 4/417 |
| ✅ | `agify_name` | 100.0% | 99.76% | 372.9 | 3237.1 | 2000ms | 1/417 |
| ✅ | `rest_countries` | 100.0% | 99.04% | 259.4 | 7269.1 | 2500ms | 4/417 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.7 | 2314.9 | 2000ms | 1/417 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/417 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5959.2 | 72.0% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5164.2 | 64.0% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `numbers_trivia` | 12:00 | 4658.8 | 44.44% |
| `nasa_apod` | 12:00 | 4598.1 | 66.67% |
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
