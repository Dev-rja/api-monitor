# API Reliability Monitor — SLA Report

> Last updated: **2026-06-27 15:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.93% | 2400.6 | 10206.7 | 1000ms | 267/1210 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 125.5 | 4595.4 | 1500ms | 4/1210 |
| ❌ | `nasa_apod` | 74.13% | 50.08% | 3362.5 | 11152.5 | 2000ms | 604/1210 |
| ❌ | `ipapi_check` | 76.94% | 99.92% | 155.6 | 4507.0 | 2500ms | 1/1210 |
| ⚠️ | `rest_countries` | 98.76% | 98.43% | 331.4 | 10221.5 | 2500ms | 19/1210 |
| ⚠️ | `open_meteo_weather` | 98.93% | 96.94% | 716.3 | 14877.1 | 2000ms | 37/1210 |
| ✅ | `useless_fact` | 99.59% | 99.67% | 632.2 | 10229.6 | 2500ms | 4/1210 |
| ✅ | `dog_ceo_random` | 99.59% | 96.53% | 543.0 | 10244.1 | 2500ms | 42/1210 |
| ✅ | `catfact_random` | 99.75% | 99.26% | 260.0 | 10080.2 | 3000ms | 9/1210 |
| ✅ | `coingecko_bitcoin` | 99.75% | 100.0% | 95.7 | 253.3 | 1500ms | 0/1210 |
| ✅ | `agify_name` | 99.92% | 99.67% | 386.7 | 16112.2 | 2000ms | 4/1210 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.7 | 3882.8 | 2000ms | 2/1210 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4355.7 | 55.77% |
| `nasa_apod` | 17:00 | 4247.7 | 55.38% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4057.3 | 61.29% |
| `nasa_apod` | 18:00 | 3824.0 | 54.1% |
| `nasa_apod` | 11:00 | 3702.0 | 53.73% |
| `nasa_apod` | 20:00 | 3585.0 | 48.72% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
