# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 11:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.59% | 3571.5 | 10206.7 | 1000ms | 138/413 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.0 | 4088.9 | 1500ms | 2/413 |
| ❌ | `nasa_apod` | 61.99% | 38.01% | 4313.2 | 10549.1 | 2000ms | 256/413 |
| ❌ | `ipapi_check` | 93.95% | 100.0% | 159.2 | 353.0 | 2500ms | 0/413 |
| ⚠️ | `open_meteo_weather` | 98.06% | 96.85% | 748.2 | 14877.1 | 2000ms | 13/413 |
| ⚠️ | `dog_ceo_random` | 99.27% | 89.83% | 880.4 | 10244.1 | 2500ms | 42/413 |
| ✅ | `catfact_random` | 99.27% | 99.27% | 276.6 | 10080.2 | 3000ms | 3/413 |
| ✅ | `useless_fact` | 99.52% | 99.03% | 587.0 | 10229.6 | 2500ms | 4/413 |
| ✅ | `agify_name` | 100.0% | 99.76% | 373.0 | 3237.1 | 2000ms | 1/413 |
| ✅ | `rest_countries` | 100.0% | 99.03% | 260.0 | 7269.1 | 2500ms | 4/413 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 233.0 | 2314.9 | 2000ms | 1/413 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/413 |

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
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |
| `numbers_trivia` | 07:00 | 4515.1 | 42.86% |
| `nasa_apod` | 14:00 | 4500.5 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
