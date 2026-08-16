# API Reliability Monitor — SLA Report

> Last updated: **2026-08-16 14:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.42% | 3492.9 | 10420.1 | 1000ms | 675/2010 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 136.1 | 5075.4 | 1500ms | 9/2010 |
| ❌ | `ipapi_check` | 58.81% | 99.95% | 145.9 | 4507.0 | 2500ms | 1/2010 |
| ❌ | `nasa_apod` | 77.91% | 53.93% | 3008.8 | 11152.5 | 2000ms | 926/2010 |
| ⚠️ | `dog_ceo_random` | 96.22% | 97.11% | 510.4 | 10244.1 | 2500ms | 58/2010 |
| ⚠️ | `open_meteo_weather` | 98.91% | 97.86% | 692.5 | 14877.1 | 2000ms | 43/2010 |
| ✅ | `rest_countries` | 99.25% | 98.96% | 280.1 | 10221.5 | 2500ms | 21/2010 |
| ✅ | `useless_fact` | 99.75% | 99.65% | 650.6 | 10229.6 | 2500ms | 7/2010 |
| ✅ | `catfact_random` | 99.75% | 99.4% | 263.7 | 10080.2 | 3000ms | 12/2010 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.0 | 4328.4 | 1500ms | 1/2010 |
| ✅ | `agify_name` | 99.9% | 99.75% | 391.5 | 16112.2 | 2000ms | 5/2010 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.8 | 3882.8 | 2000ms | 2/2010 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5258.2 | 52.5% |
| `numbers_trivia` | 02:00 | 4528.0 | 42.86% |
| `numbers_trivia` | 10:00 | 4472.8 | 42.86% |
| `nasa_apod` | 05:00 | 4196.2 | 58.82% |
| `numbers_trivia` | 14:00 | 4176.1 | 40.66% |
| `numbers_trivia` | 05:00 | 4102.4 | 39.22% |
| `nasa_apod` | 02:00 | 3934.2 | 57.14% |
| `numbers_trivia` | 09:00 | 3846.3 | 37.21% |
| `nasa_apod` | 03:00 | 3832.5 | 57.5% |
| `numbers_trivia` | 07:00 | 3703.5 | 35.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
