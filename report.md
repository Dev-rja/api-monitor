# API Reliability Monitor — SLA Report

> Last updated: **2026-04-19 21:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 71.06% | 3134.5 | 10206.7 | 1000ms | 112/387 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 121.4 | 3806.8 | 1500ms | 1/387 |
| ❌ | `nasa_apod` | 63.57% | 39.79% | 4132.2 | 10538.0 | 2000ms | 233/387 |
| ❌ | `ipapi_check` | 93.8% | 100.0% | 159.6 | 353.0 | 2500ms | 0/387 |
| ⚠️ | `open_meteo_weather` | 97.93% | 96.9% | 752.5 | 14877.1 | 2000ms | 12/387 |
| ⚠️ | `dog_ceo_random` | 99.22% | 89.15% | 912.4 | 10244.1 | 2500ms | 42/387 |
| ✅ | `useless_fact` | 99.48% | 98.97% | 589.3 | 10229.6 | 2500ms | 4/387 |
| ✅ | `catfact_random` | 99.48% | 99.74% | 245.8 | 10070.5 | 3000ms | 1/387 |
| ✅ | `agify_name` | 100.0% | 99.74% | 371.9 | 3237.1 | 2000ms | 1/387 |
| ✅ | `rest_countries` | 100.0% | 98.97% | 261.5 | 7269.1 | 2500ms | 4/387 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.74% | 234.6 | 2314.9 | 2000ms | 1/387 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/387 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 17:00 | 5580.9 | 69.57% |
| `nasa_apod` | 03:00 | 5533.2 | 90.0% |
| `nasa_apod` | 18:00 | 5312.9 | 81.25% |
| `numbers_trivia` | 00:00 | 5183.1 | 50.0% |
| `nasa_apod` | 11:00 | 4750.3 | 60.87% |
| `nasa_apod` | 14:00 | 4584.8 | 60.87% |
| `nasa_apod` | 21:00 | 4556.5 | 50.0% |
| `nasa_apod` | 20:00 | 4536.6 | 66.67% |
| `nasa_apod` | 12:00 | 4380.0 | 62.5% |
| `nasa_apod` | 13:00 | 4333.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
